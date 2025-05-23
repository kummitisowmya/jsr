from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class QuestionAnswer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    numbers=models.JSONField()
    answer=models.IntegerField()
    submittedat=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.correct_answer}"

