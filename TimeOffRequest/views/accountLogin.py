from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from TimeOffRequest.forms import EmployeeProfileForm
from TimeOffRequest.models import Employee


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class EmployeeRegistrationView(CreateView):
    model = Employee
    form_class = EmployeeProfileForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
