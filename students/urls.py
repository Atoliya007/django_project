from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.get_students, name='get_students'),
    path('/<int:pk>', views.get_student_by_id, name='get_student_by_id'),
    path('/create', views.create_student, name='create_student'),
    path('/update/<int:id>', views.update_student, name='update_student'),
    path('/delete/<int:id>', views.delete_student, name='delete_student'),
    path('/fetch/', views.filter_data, name='filter_data'),
]
