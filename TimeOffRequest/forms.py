from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from .models.TimeOffRequestModel import TimeOffRequestModel


class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequestModel
        fields = ['employee_id', 'first_name', 'last_name', 'request_start', 'request_end', 'reason', 'approval']

class EmployeeProfileForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'password1', 'password2', 'employee_id']