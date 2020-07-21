from django.shortcuts import render


# Create your views here.
# views.py
from rest_framework import viewsets

##################################################
from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('first_name')
    serializer_class = StudentSerializer
##################################################

from .serializers import TeacherSerializer
from .models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('submission_date')
    serializer_class = TeacherSerializer
###################################################
    from .serializers import SubmissonSerializer
from .models import Submisson


class SubmissonViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('submission_date')
    serializer_class = TeacherSerializer
