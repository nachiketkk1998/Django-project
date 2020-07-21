# serializers.py
from rest_framework import serializers

############################################
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'Subject', 'student_Id', 'submission_date')
############################################
from rest_framework import serializers

from .models import Teacher

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('Subject', 'teacher_Id', 'submission_date', 'submission')
############################################
from .models import Submission

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('Subject', 'teacher_Id', 'submission_date', 'student_Fullname','student_Id')
        
############################################   
