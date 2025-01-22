from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg, Sum

# Work with DataBase
# Transform Data
# Data Pass
# HTTP Response / JSON Response

# Create your views here.
# def home(request):
#     return HttpResponse("Welcome to the task management system")

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

# def test(request):
#     context = {
#         "names": {"Mahmud", "Hasan", "Shamim", "Mr. X"},
#         "ages": {23, 25, 27},
#     }
#     return render(request, "test.html", context)

def test(request):
    names = ["Mahmud", "Hasan", "Shamim", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "ages": {23, 25, 27},
        "count": count,
    }
    return render(request, "test.html", context)


def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm() # For GET. By default GET method thake, tay GET bola lagbe na

    if request.method == "POST": # For POST method.
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """ For Model Form Data """
            form.save()

            return render(request, 'task_form.html', {"form": form, "message": "task added successfully"})

            # For Django Form Data 
            '''
            data = form.cleaned_data
            title = data.get("title")
            description = data.get("description")
            due_date = data.get("due_date")
            assigned_to = data.get("assigned_to") # list [1, 3]

            task = Task.objects.create(
                title = title,
                description = description,
                due_date = due_date
            )

            # Assign employee to tasks 
            for emp_id in assigned_to:
                employee = Employee.objects.get(id = emp_id)
                task.assigned_to.add(employee)

            return HttpResponse("Task Added Successfully.")
            '''

    context = { "form": form }
    return render(request, "task_form.html", context)

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


def view_task(request):
    # task_count = Task.objects.aggregate(num_task = Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})