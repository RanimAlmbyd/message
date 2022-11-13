from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=20)        
    recipient = models.CharField(max_length=20)        
    send_date = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=20)
    text=models.CharField(max_length=300)
    read = models.BooleanField(default=False)
    