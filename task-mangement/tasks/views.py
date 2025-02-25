from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskModelForm, TaskDetailModelForm
from tasks.models import Task, Project
from django.db.models import Q, Count
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from users.views import is_admin
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, DetailView, UpdateView, TemplateView


def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Employee').exists()


# Manager Decorator 
manager_dashboard_decorators = [
    login_required(login_url='no-permission'),
    permission_required('tasks.view_task', login_url='no-permission'),
]

@method_decorator(manager_dashboard_decorators, name='dispatch')
class ManagerDashboard(View):
    template_name = 'dashboard/manager-dashboard.html'

    def get(self, request, *args, **kwargs):
        type = request.GET.get('type', 'all')

        counts = Task.objects.aggregate(
            total = Count('id'),
            completed = Count('id', filter = Q(status = 'COMPLETED')),
            in_progress = Count('id', filter = Q(status = 'IN_PROGRESS')),
            pending = Count('id', filter = Q(status = 'PENDING')),
        )

        # Retriving task data 
        base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

        if type == 'completed':
            tasks = base_query.filter(status = 'COMPLETED')
        elif type == 'in-progress':
            tasks = base_query.filter(status = 'IN_PROGRESS')
        elif type == 'pending':
            tasks = base_query.filter(status = 'PENDING')
        elif type == 'all':
            tasks = base_query.all()

        context = {
            'tasks': tasks,
            'counts': counts,
            'role': 'manager',
        }

        return render(request, self.template_name, context)


# Employee dashboard 
class EmployeeDashboard(UserPassesTestMixin, TemplateView):
    template_name = "dashboard/user-dashboard.html"

    def test_func(self):  
        return self.user_is_employee() # test_func() builin

    def user_is_employee(self):  
        return self.request.user.groups.filter(name='Employee').exists()

    def handle_no_permission(self):
        return redirect('no-permission')


# Create Task 
create_decorators = [
    login_required,
    permission_required("tasks.add_task", login_url="no-permission")
]

@method_decorator(create_decorators, name='dispatch')
class CreateTask(ContextMixin, LoginRequiredMixin, PermissionRequiredMixin, View):
    """ For creating task """
    permission_required = 'tasks.add_task'
    login_url = 'sign-in'
    template_name = "task_form.html"

    """
    0. Create Task
    1. LoginRequiredMixin
    2. PermissionRequiredMixin
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_form'] = kwargs.get('task_form', TaskModelForm())
        context['task_details_form'] = kwargs.get(
            'task_details_form', TaskDetailModelForm()
        )
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST, request.FILES)

        if task_form.is_valid() and task_detail_form.is_valid():

            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Created Successfully")
            return redirect('create-task')
        else:
            context = self.get_context_data(
                task_form = task_form,
                task_detail_form = task_detail_form
            )
            return render(request, self.template_name, context)


# Update Task 
update_decorators = [
    login_required,
    permission_required("tasks.change_task", login_url="no-permission")
]

@method_decorator(update_decorators, name="dispatch")
class UpdateTaskView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["id"])
        task_form = TaskModelForm(instance=task)
        task_detail_form = None
        if hasattr(task, "details"):  
            task_details_form = TaskDetailModelForm(instance=task.details)

        context = {"task_form": task_form, "task_details_form": task_details_form}
        return render(request, "task_form.html", context)


    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["id"])
        task_form = TaskModelForm(request.POST, instance=task)
        task_details_form = TaskDetailModelForm(request.POST, instance=task.details) if hasattr(task, "details") else None

        if task_form.is_valid() and (task_details_form is None or task_details_form.is_valid()):
            task = task_form.save()
            if task_details_form:
                task_detail = task_details_form.save(commit=False)
                task_detail.task = task
                task_detail.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id=task.id)

        return render(request, "task_form.html", {
            "task_form": task_form,
            "task_details_form": task_details_form
        })


# Use this class 
@method_decorator(update_decorators, name="dispatch")
class UpdateTask(UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'task_form.html'
    context_object_name = 'task'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_form'] = self.get_form()
        if hasattr(self.object, 'details') and self.object.details:
            context['task_details_form'] = TaskDetailModelForm(
                instance=self.object.details)
        else:
            context['task_details_form'] = TaskDetailModelForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        task_form = TaskModelForm(request.POST, instance=self.object)

        task_details_form = TaskDetailModelForm(
            request.POST, request.FILES, instance=getattr(self.object, 'details', None))

        if task_form.is_valid() and task_details_form.is_valid():

            """ For Model Form Data """
            task = task_form.save()
            task_details = task_details_form.save(commit=False)
            task_details.task = task
            task_details.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', self.object.id)
        return redirect('update-task', self.object.id)


@login_required
@permission_required("tasks.delete_task", login_url="no-permission")
def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Something went wrong!')
        return redirect('manager-dashboard')


view_project_decorator = [login_required, permission_required(
    "projects.view_project",
    login_url='no-permission'
)]

@method_decorator(view_project_decorator, name='dispatch')
class ViewProject(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'show_task.html'

    def get_queryset(self):
        querset = Project.objects.annotate(
            num_task = Count('task')).order_by('num_task')
        return querset


class TaskDetails(DetailView):
    model = Task
    template_name = 'task_details.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # {"task": task}
        context['status_choices'] = Task.STATUS_CHOICES # {"task": task, 'status_choices': status_choices}
        return context
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        selected_status = request.POST.get('task_status')
        task.status = selected_status
        task.save()
        return redirect('task-details', task.id)


@login_required
def dashboard(request):
    if is_manager(request.user):
        return redirect('manager-dashboard')
    elif is_employee(request.user):
        return redirect('user-dashboard')
    if is_admin(request.user):
        return redirect('admin-dashboard')
    
    return redirect('no-permission')