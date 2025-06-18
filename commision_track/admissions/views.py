

# Create your views here.
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import StudentForm
from django.contrib import messages
from .models import Student
from .forms import CommissionForm
from .models import CommissionDetails

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Data Saved Succesfully")
            return redirect('add-student')  # refresh after saving
    else:
        form = StudentForm()
    return render(request, 'Admission_form.html', {'form': form})

def add_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    commission = CommissionDetails.objects.filter(student=student).first()

    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        if form.is_valid():
            commission = form.save(commit=False)
            commission.student = student
            commission.save()
            messages.success(request,"Commision Details Added Succesfully")
            return redirect('/accounts_first_page')
    else:
        form = CommissionForm(instance=commission)

    return render(request, 'accounts_form.html', {'student': student, 'form': form})
