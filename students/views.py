from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
# Create new student record
@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all students (with optional filters)
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    page  = request.GET.get("page")
    limit  = request.GET.get("limit")
    paginator = Paginator(students,limit)
    page_obj = paginator.get_page(page)               
    page_data = list(paginator.object_list.values())
    data = list(page_obj.object_list.values())
    return JsonResponse({
        'page': page_obj.number,
        'total_pages': paginator.num_pages,
        'total_items': paginator.count,
        'data': data,
    })
    # Example filter: ?gender=Male
    gender = request.query_params.get('gender', None)
    if gender:
        students = students.filter(gender=gender)

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

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

@api_view(['GET'])
def filter_data(request):
    students = Student.objects.all()
    if request.method == 'GET':
        st = request.GET.get('name')
        students = Student.objects.filter(name=st)
    return JsonResponse({
        'name': st
    })

