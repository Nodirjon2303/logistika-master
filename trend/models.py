from django.db import models

# Create your models here.


class Trend(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    img=models.ImageField(upload_to="static/trend/img")

    def __str__(self):
        return self.title

