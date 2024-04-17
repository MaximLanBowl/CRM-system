import datetime

from django.db import models
from django.utils import timezone

from contacts.models import Contact
from products.models import Product


class Task(models.Model):
    objects = None
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=Contact)
    title = models.CharField(max_length=150, default='start')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=Product)
    start_date = models.DateField()
    end_date = models.DateField()
    due_date = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=status_choices)

    def __str__(self):
        return f'Task for {self.contact} - {self.product}'

    def is_due_soon(self):
        now = timezone.now()
        return str(self.due_date) <= now + timezone.timedelta(days=1)

