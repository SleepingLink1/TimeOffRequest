from django import forms
# TODO: create time off request form
class TimeOffRequestForm(forms.Form):
    employee_id = forms.IntegerField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    request_start = forms.DateField()
    request_end = forms.DateField()
    reason = forms.CharField(widget=forms.Textarea)