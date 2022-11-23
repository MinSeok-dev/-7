from django.db import models

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    
class AiModel(models.Model):
    ai_file = models.FileField(blank=True)
    version = models.CharField(max_length=100)
    is_selected = models.BooleanField(default = False)
    pub_date = models.DateTimeField('date published')
    

