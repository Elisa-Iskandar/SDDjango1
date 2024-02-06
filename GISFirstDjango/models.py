from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=False, null=True)

class TeachingGroup(models.Model):
    name = models.CharField(max_length=30, null=True)
    students = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    year_group = models.IntegerField(blank=False, null=True)


class Student(Person):
    year = models.IntegerField()
    tutor_room = models.CharField(max_length=3, blank=True)

class Teacher(Person):
    tutor_room = models.CharField(max_length=3, blank=True)
    subject = models.CharField(max_length=30)
