from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Role (models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.title

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    classroom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school_code = models.IntegerField()
    Role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    
    def __str__(self) :
        return self.user.first_name


class Parent (models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.first_name
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    student_result = models.CharField(max_length=100)
    slug = models.SlugField()
    Parent = models.ForeignKey(Parent, on_delete=models.DO_NOTHING)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

