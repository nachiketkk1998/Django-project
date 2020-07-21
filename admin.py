from django.contrib import admin

# Register your models here.
from .models import Student
admin.site.register(Student)
##################################
from .models import Teacher
admin.site.register(Teacher)
##################################
from .models import Parents
admin.site.register(Parents)
##################################
from .models import Fees_payment
admin.site.register(Fees_payment)
##################################
from .models import Submission
admin.site.register(Submission)
