from django.db import models


# Create your models here.

class employees(models.Model):
    firstname =models.CharField(max_length=50) 
    lastname = models.CharField(max_length=50)
    empId = models.IntegerField()
    
def _str_(self):
    return self.firstname
    


    
    
