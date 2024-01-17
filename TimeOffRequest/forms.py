from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
class TimeOffRequestForm(forms.Form):
    employee_id = forms.IntegerField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    request_start = forms.DateField()
    request_end = forms.DateField()
    reason = forms.CharField(widget=forms.Textarea)

class EmployeeProfileForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'password1', 'password2', 'employee_id']