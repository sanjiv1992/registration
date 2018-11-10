from django.db import models

# Create your models here.
class userform(models.Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    discription=models.CharField(max_length=50)
    file=models.FileField(upload_to='docs/')