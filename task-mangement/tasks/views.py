from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg, Sum
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from users.views import is_admin
from django.views import View


# Class based View Re-use example 
class Greetings(View):
    greetings = 'Hello Everyone'

    def get(self, request):
        return HttpResponse(self.greetings)
    

class HiGreetings(Greetings):
    greetings = 'Hi Everyone'


class HiHowGreetings(Greetings):
    greetings = 'Hi Everyone, How are you?'


def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Manager').exists()

@user_passes_test(is_manager, login_url='no-permission')
def manager_dashboard(request):
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
    return render(request, "dashboard/manager-dashboard.html", context)

# CURD 
# C = CREATE 
# R = READ 
# U = UPDATE 
# D = DELETE 

@user_passes_test(is_employee)
def employee_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

@login_required
@permission_required("tasks.add_task", login_url="no-permission")
def create_task(request):
    # employees = Employee.objects.all()
    task_form = TaskModelForm() # For GET. By default GET method thake, tay GET bola lagbe na
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST": # For POST method.
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
        
    context = { "task_form": task_form, "task_detail_form": task_detail_form }
    return render(request, "task_form.html", context)


@login_required
@permission_required("tasks.change_task", login_url="no-permission")
def update_task(request, id):
    task = Task.objects.get(id=id)
    # employees = Employee.objects.all()
    task_form = TaskModelForm(instance=task) # For GET. By default GET method thake, tay GET bola lagbe na

    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)

    if request.method == "POST": # For POST method.
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid():
            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id)
        
    context = { "task_form": task_form, "task_detail_form": task_detail_form }
    return render(request, "task_form.html", context)


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


@login_required
@permission_required("tasks.view_task", login_url="no-permission")
def view_task(request):
    # task_count = Task.objects.aggregate(num_task = Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})


@login_required
@permission_required("tasks.view_task", login_url="no-permission")
def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    status_choices = Task.STATUS_CHOICES

    if request.method == 'POST':
        selected_status = request.POST.get('task_status')
        task.status = selected_status
        task.save()
        return redirect('task-details', task.id)

    return render(request, 'task_details.html', {"task": task, 'status_choices': status_choices})


@login_required
def dashboard(request):
    if is_manager(request.user):
        return redirect('manager-dashboard')
    elif is_employee(request.user):
        return redirect('user-dashboard')
    if is_admin(request.user):
        return redirect('admin-dashboard')
    
    return render('no-permission')