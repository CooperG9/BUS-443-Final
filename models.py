from django.db import models

class Studentdetails(models.Model):
	studentid = models.IntegerField()
	firstname = models.CharField(max_length=500)
	lastname = models.CharField(max_length=500)
	major = models. TextField()
	year = models. TextField()
	gpa = models.CharField(max_length=500)

class Course(models.Model):
	courseid = models.IntegerField()
	coursetitle = models.CharField(max_length=500)
	coursename = models.CharField(max_length=500)
	coursecode = models.CharField(max_length=500)
	coursedep = models.CharField(max_length=500)
	courseinstructor = models.CharField(max_length=500)

class Enrollment(models.Model):
	courseid = models.IntegerField()
	coursetitle = models.CharField(max_length=500)
	coursename = models.CharField(max_length=500)
	coursecode = models.CharField(max_length=500)
	coursedep = models.CharField(max_length=500)
	courseinstructor = models.CharField(max_length=500)


# Create your models here.
