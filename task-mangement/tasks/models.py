from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.

# 3. Many to Many 
# task = onek gula employee akta task korse
# akta employee = onek gula task er jonno assign ase 
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # tasks

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    project = models.ForeignKey(
        "Project",
        on_delete=models.DO_NOTHING,
        default=1
    )
    assigned_to = models.ManyToManyField(Employee, related_name='tasks')
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="PENDING",
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # details 

    def __str__(self):
        return self.title


# ***** Relationship 
# 1. One to One 
# 2. Many to One 
# 3. Many to Many 

# 1. One to One -->
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )

    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='details'
    )
    # assigned_to = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_OPTIONS,
        default=LOW
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details form Task {self.task.title}"

# Task.objects.get(id=2) 
# select * from task where id = 2 
# ORM 

# 2. Many to One 
class Project (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name

# Signals 

@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_task_creation(sender, instance, action, **kwargs):
    if action == 'post_add':
        assigned_emails = [emp.email for emp in instance.assigned_to.all()]
        print("Checking...", assigned_emails)

        send_mail(
            "New Task Assigned",
            f"You have been assigned to the task: {instance.title}",
            "slashupdates@gmail.com",
            assigned_emails,
            fail_silently=False,
        )


@receiver(post_delete, sender=Task)
def delete_associate_details(sender, instance, **kwargs):
    if instance.details:
        print(isinstance)
        instance.details.delete()

        print("Deleted successfully")
        