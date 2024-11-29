from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    rollno = models.CharField(max_length=50, unique=True)
    father_name = models.CharField(max_length=255)
    section = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.rollno})"

# Create your models here.
