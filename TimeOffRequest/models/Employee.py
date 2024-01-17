from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(unique=True)

    class Meta:
        app_label = 'TimeOffRequest'

    def __str__(self):
        return self.user.username