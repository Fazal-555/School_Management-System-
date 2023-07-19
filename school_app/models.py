from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name
