from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithFileField
 from django.db.models import FloatField

class Student(models.Model):
    Students_first_name = models.CharField(max_length=50)
    Students_last_name = models.CharField(max_length=50)
    student_ID_NO= models.CharField(max_length=100, primary_key=True)
    Subject = models.CharField(max_length=100)
    Cuurent_academic_grade= models.IntegerField()
    Submission_date= models.DateField()

   
class Teacher(models.Model):
    teacher-name= models.CharField(max_length=100)
    teacher_Id= models.CharField(max_length=100,primary_key=True)
    Subject = models.CharField(max_length=100)
    Students= models.ForeignKey(student_Id, on_delete=models.CASCADE)

class Parents(models.Model)

     Marking_Scheme = (
        ('AA', '10/10'),
        ('AB,  '9/10'),
        ('BB', '8/10'),
        ('BC', '7/10'),
        ('CC', '6/10'),
        ('FF', 'Retest'),
       
    Student_name = models.CharField(max_length=50)
    student_Id= models.IntegerField()
    Subject = models.CharField(max_length=100)
    Teacher_Remarks= models.CharField(max_length=1, choices=Worksheet_Marking


class Fees_payment(models.Model)
       
    Student_Fullname = models.CharField(max_length=50)
    student_Id= models.CharField(max_length=100, primary_key=True)
    Academic_year=pages = models.IntegerField()
    No_of_Subjects=pages = models.IntegerField()
   Fees_payment.objects.sum( Fees_Due=Max('No_of_Subjects', output_field=FloatField()) * 3400)
   {'Fees_Due': Rs 10,000/-}

class Submission(models.Model)
       
    Student_Fullname = models.CharField(max_length=50)
    student_Id= models.CharField(max_length=100, primary_key=True)
    teacher_Id= models.CharField(max_length=100)
    Subject= models.CharField(max_length=50)
    Submission_date= models.DateField()
   

def upload_Assingment(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})
