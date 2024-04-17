from django.db import models


class Employee(models.Model):
    objects = None
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.CharField(max_length=50, default='ADMIN')

    @property
    def __str__(self):
        return self.user.username