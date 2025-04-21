from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import title


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=[
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ])


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="users/teacher/", null=True, blank=True)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.user



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="users/student/", null=True, blank=True)

    def __str__(self):
        return self.user