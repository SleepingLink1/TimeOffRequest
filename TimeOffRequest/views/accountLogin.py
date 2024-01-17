from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import EmployeeProfileForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

class EmployeeRegistrationView(CreateView):
    model = Employee
    form_class = EmployeeProfileForm
    template_name = 'accounts/employee_registration.html'
    success_url = reverse_lazy('login')