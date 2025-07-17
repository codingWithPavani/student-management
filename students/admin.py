from django.contrib import admin

# Register your models here.

from .models import Student

admin.site.register(Student)  # Register the Student model to the admin site
