from django.db import models

# Create your models here.
class Page(models.Model):
    page_id=models.CharField(max_length=100)
    access_token=models.CharField(max_length=300)
    prefix=models.CharField(max_length=100)
    post_count=models.IntegerField()
