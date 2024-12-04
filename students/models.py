from django.db import models
from datetime import datetime
from django.utils import timezone
class Student(models.Model):
    name = models.CharField(max_length=255)
    rollno = models.CharField(max_length=50, unique=True)
    father_name = models.CharField(max_length=255)
    section = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default = False)

    def __str__(self):
        return f"name={self.name}, deleted={self.deleted}, rollno=({self.rollno})"

    def delete_student(self):
        self.deleted = True
        self.save()
    
# Create your models here.
