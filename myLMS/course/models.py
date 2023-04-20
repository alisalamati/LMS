from django.db import models

# Create your models here.

class Department(models.Model):
    code = models.CharField(max_length = 5)
    title = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20, default='default')
    #will_delete = models.CharField(max_length = 20, default='default')
    def __str__(self):
        return("%s %s" % (self.title, self.code))
   
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    code = models.CharField(max_length = 5)
    title = models.CharField(max_length = 20)
    
