from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll =models.IntegerField()
    per = models.FloatField()

    def __str__(self):
        return str((self.id,self.name,self.roll,self.per))

