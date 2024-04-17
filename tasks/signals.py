from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from notifications.signals import notify

from .models import Task


@receiver(pre_save, sender=Task)
def notify_due_date(sender, instance, **kwargs):
    if instance.is_due_soon():
        notify.send(sender=instance, recipient=instance.created_by, verb='Due date soon!',
                    description=f'The due date for the task "{instance.name}" is approaching.')
