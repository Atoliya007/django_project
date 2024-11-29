from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_students, name='get_students'),
    path('students/<int:pk>/', views.get_student_by_id, name='get_student_by_id'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/update/<int:pk>/', views.update_student, name='update_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]
