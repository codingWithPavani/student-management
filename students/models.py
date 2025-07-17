from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"