from django.core.mail import send_mail


def send_notification(task):
    send_mail('Reminder', 'Task deadline is approaching', 'from@example.com', ['to@example.com'])
