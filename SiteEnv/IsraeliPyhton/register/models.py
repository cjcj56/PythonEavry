from django.db import models
#from django.db.models import User
#from django.contrib.auth import User


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50,blank=False)
    username = models.CharField(max_length=30,blank=False)
    password = models.CharField(max_length=30,blank=False)
    last_page = models.CharField(max_length=15)

	#def __init__(self,firstname,lastname,email,username,password):
	#	super.__init__(self)


    def __str__(self):
        return self.get_full_name()

