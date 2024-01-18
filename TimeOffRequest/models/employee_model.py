from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    employee_id = models.IntegerField(unique=True)
    password = models.CharField(max_length=30)


    def save(self, *args, **kwargs):
        self.username = self.employee_id
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.employee_id} {self.first_name} {self.last_name}"