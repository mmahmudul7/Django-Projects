from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Prefetch
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView, UpdateView, FormView, ListView
from users.forms import LoginForm, CustomRegistrationForm, AssignRoleForm, CreateGroupForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm, EditProfileForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views import View


# Test for users
def is_admin(user):
    return user.groups.filter(name='Admin').exists()


User = get_user_model()

# Edit User Profile
class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/update_profile.html'
    context_object_name = 'form'

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return redirect('profile')


# Sign Up View 
class SignUp(FormView):
    template_name = 'registration/register.html'
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('sign-in')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password1'))
        user.is_active = False
        user.save()
        messages.success(self.request, 'A Confirmation mail sent. Please check your email')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is not valid")
        return self.render_to_response(self.get_context_data(form=form))


# Login
class CustomLoginView(LoginView):
    form_class = LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else super().get_success_url()


# Change Password view
class ChangePassword(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = CustomPasswordChangeForm


# Sign out "from django.contrib.auth.views import LogoutView" in url


# FBV
def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')


# Admin Dashboard View
admin_dashboard_decorators = [
    user_passes_test(is_admin, login_url='no-permission'),
]

@method_decorator(admin_dashboard_decorators, name='dispatch')
class AdminDashboard(TemplateView):
    template_name = 'admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.prefetch_related(
            Prefetch('groups', queryset=Group.objects.all(), to_attr='all_groups')
        ).all()

        for user in users:
            user.group_name = user.all_groups[0].name if user.all_groups else 'No Group Assigned'

        context["users"] = users
        return context


# Assign Role View
@method_decorator(admin_dashboard_decorators, name='dispatch')
class AssignRole(View):
    template_name = 'admin/assign_role.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = AssignRoleForm()
        return render(request, self.template_name, {"form": form, "user": user})

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = AssignRoleForm(request.POST)

        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin-dashboard')

        return render(request, self.template_name, {"form": form, "user": user})


# Create Group View
@method_decorator(admin_dashboard_decorators, name='dispatch')
class CreateGroup(View):
    template_name = 'admin/create_group.html'

    def get(self, request):
        form = CreateGroupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully")
            return redirect('create-group')

        return render(request, self.template_name, {'form': form})


# Group List View
@method_decorator(admin_dashboard_decorators, name='dispatch')
class GroupList(ListView):
    model = Group
    template_name = 'admin/group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return Group.objects.prefetch_related('permissions').all()


# FBV
@user_passes_test(is_admin, login_url='no-permission')
def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'admin/group_list.html', {'groups': groups})


# Profile View
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['username'] = user.username
        context['email'] = user.email
        context['name'] = user.get_full_name()
        context['bio'] = user.bio
        context['profile_image'] = user.profile_image

        context['member_since'] = user.date_joined
        context['last_login'] = user.last_login

        return context


# Custom Change Password Reset View
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/reset_password.html'
    success_url = reverse_lazy('sign-in')
    html_email_template_name = 'registration/reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'https' if self.request.is_secure() else 'http'
        context['domain'] = self.request.get_host()
        print(context)
        return context

    def form_valid(self, form):
        messages.success(
            self.request, 'A Reset eamil sent. Please check your email'
        )
        return super().form_valid(form)


# Custom Password Reset Confirm View
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'registration/reset_password.html'
    success_url = reverse_lazy('sign-in')

    def form_valid(self, form):
        messages.success(
            self.request, 'Password reset successfully'
        )
        return super().form_valid(form)


""" 

    Admin
        - Sobkisui
    Manager
        - project
        - task create
    Employee
        - Task read
        - Task update
    
    Role Based Access Control (RBAC)
"""