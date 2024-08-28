from django.db import models

# Create your models here.

class Worker(models.Model):
    Name = models.CharField(max_length=20)
    salary =models.IntegerField()
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name