from django.db import models


class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='client_photos/', null=True, blank=True)
    email = models.EmailField(default='Почта')
    phone = models.IntegerField(default='Номер телефона')
    documents = models.TextField(blank=True)
    information = models.TextField(blank=True)


class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
