from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskDb(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(default="Pending")

    def __str__(self):
        return self.title

