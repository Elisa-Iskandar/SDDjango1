from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class TeachingGroup(models.Model):
    students = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)

class Student(Person):
    year = models.IntegerField()
    tutor_room = models.CharField(max_length=3, blank=True)

class Teacher(Person):
    tutor_room = models.CharField(max_length=3, blank=True)
    subject = models.CharField(max_length=30)