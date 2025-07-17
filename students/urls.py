from . import views
from django.urls import path
# from .views import add_student
urlpatterns = [
    path('add/', views.add_student, name='add_student'),  # URL for adding a student
    path('', views.student_list, name='student_list'),  # URL for listing students
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),  # URL for editing a student
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]