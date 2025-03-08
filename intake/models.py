from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(default=timezone.localtime)

def __str__(self):
        return f"{self.user.username} - {self.quantity}L on {self.date} and {self.time}"