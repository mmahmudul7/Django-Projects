from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg, Sum
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required


def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

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
        task_detail_form = TaskDetailModelForm(request.POST)
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

# def view_task(request):
#     # retrive all data from tasks model 
#     tasks = Task.objects.all()

#     # retrive a specific task 
#     task_3 = Task.objects.get(id=3)

#     # Fetch the first task 
#     first_task = Task.objects.first()
#     return render(request, "show_task.html", {"tasks": tasks, "task3": task_3, "first_task": first_task})

# def view_task(request):
#     ''' Show the tasks that are Pending '''
#     # tasks = Task.objects.filter(status="PENDING")

#     ''' Show the task which due date is today '''
#     # tasks = Task.objects.filter(due_date = date.today())

#     ''' Show the task whose priority is not Low '''
#     # tasks = TaskDetail.objects.exclude(priority='L')

#     ''' Show the task that contain word "paper" '''
#     # tasks = Task.objects.filter(title__contains = "paper")

#     ''' Show the task that contain letter capital "C" and status is "Pending" '''
#     # tasks = Task.objects.filter(title__contains = "C", status = "PENDING")

#     ''' Show the task which are status is "Pending" or "in-progress" '''
#     # tasks = Task.objects.filter(Q(status = "PENDING") | Q(status = "IN_PROGRESS"))

#     ''' Se kokhono error dibe na '''
#     # tasks = Task.objects.filter(status = "Not Existing")

#     ''' Return boolean value '''
#     # tasks = Task.objects.filter(status = "Not Existing").exists() # False
#     tasks = Task.objects.filter(status = "PENDING").exists() # True
#     return render(request, "show_task.html", {"tasks": tasks})

# def view_task(request):
#     ''' select_related (ForeignKey, OneToOneField)  '''
#     # tasks = Task.objects.select_related('details').all()
#     # tasks = TaskDetail.objects.select_related('task').all()
#     # tasks = Task.objects.select_related('details').all()

#     ''' prefetch_related (reverse ForeignKey) '''
#     # tasks = Project.object.all()

#     ''' prefetch_related (manyToMany) '''
#     tasks = Task.objects.prefetch_related("assigned_to").all()
#     return render(request, "show_task.html", {"tasks": tasks})


@login_required
@permission_required("tasks.view_task", login_url="no-permission")
def view_task(request):
    # task_count = Task.objects.aggregate(num_task = Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})