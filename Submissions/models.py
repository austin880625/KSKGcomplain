from django.db import models

# Create your models here.
class Submission(models.Model):
    context=models.TextField(blank=False)
    submit_time=models.DateTimeField(auto_now_add=True)
