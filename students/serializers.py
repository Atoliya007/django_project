from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rollno', 'father_name', 'section', 'gender', 'date_of_birth', 'student_class','created_date','updated_date','deleted']
