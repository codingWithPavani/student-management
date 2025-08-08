
from django.shortcuts import render,redirect
from .models import Student
from .forms import studentForm


def add_student(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else: 
        form = studentForm()    
    return render(request, 'students/add_student.html', {'form': form})
    

def student_list(request):
    student = Student.objects.all()
    return render(request,'students/student_list.html', {'students': student})


def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = studentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = studentForm(instance=student)
    return render(request,'students/add_student.html',{'form':form})



def delete_student(request, pk):    
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})
   



   
