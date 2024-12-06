from django.shortcuts import render
from django.http import JsonResponse
import pickle
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q
from .models import Student
from .serializers import StudentSerializer
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from django.db import connection
from django_filters.rest_framework import DjangoFilterBackend

# Create new student record
@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get a student data
@api_view(['GET'])
def get_students(request):
    name = request.GET.get('name')
    father_name = request.GET.get('father_name')
    limit = int(request.GET.get('limit', 10))  # Number of records per page
    page = int(request.GET.get('page', 1))
    
    count = 0
    if (limit < 0 or limit > 100):
        limit = 10

    offset = 0
    if (page - 1 > 0):
        offset = (page - 1) * limit
    
    
    print(offset)

    query = ""
    params = []
    if (name):
        query = query + f" and name like %s"
        params.append(f"%{name}%")

    if(father_name):
        query = query + f" and father_name like %s"
        params.append(f"%{father_name}%")

   




    with connection.cursor() as cursor:
        cursor.execute('SELECT count(id) FROM students_student WHERE id != -1'+query, params)
        # get a single line from the result
        row = cursor.fetchone()
        # get the value in the first column of the result (the only column)
        count = row[0]

    query = query + f" limit %s offset %s"
    params.append(limit)
    params.append(offset)

    print(query)
    data = []
    for row in Student.objects.raw("SELECT * FROM students_student WHERE id != -1" + query, params):
        data.append(StudentSerializer(row).data)

    return JsonResponse({
        'data': data,
        'limit': limit,
        'count': count
    })


# Get a student by ID
@api_view(['GET'])
def get_student_by_id(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student)
    return Response(serializer.data)

# Update student details
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete student record
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(student)
    student.delete_student()
    student = Student.objects.get(id=id)
    print(student)
    serializer = StudentSerializer(student)
    return Response(serializer.data)



 
    





