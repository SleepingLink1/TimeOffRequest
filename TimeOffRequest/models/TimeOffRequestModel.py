from django.db import models


# TODO: create models to store information in DB

class TimeOffRequestModel(models.Model):
    employee_id = models.IntegerField(max_length=6, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    request_start = models.DateTimeField(null=False)
    request_end = models.DateTimeField(null=False)
    reason = models.CharField(max_length=1000, blank=True, null=True)
    approval = bool(null=True)
