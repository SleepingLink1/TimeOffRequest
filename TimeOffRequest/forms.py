from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from .models.time_off_request_model import TimeOffRequestModel


class LoginForm(forms.Form):
    employee_id = forms.CharField(label='Employee ID', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequestModel
        fields = ['employee_id', 'first_name', 'last_name', 'request_start', 'request_end', 'reason', 'approval']

class EmployeeProfileForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'password1', 'password2', 'employee_id']