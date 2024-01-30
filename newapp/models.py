from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Admission(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='admissionuser',null=True,blank=True)
    sname = models.CharField(max_length = 100)
    rollno = models.CharField(max_length = 50)
    classes = models.CharField(max_length = 30)
    mothername = models.CharField(max_length=30)
    gender = models.CharField(max_length = 50)
    grno = models.CharField(max_length = 50)
    religion = models.CharField(max_length = 50)
    doa = models.DateField(auto_now=False, auto_now_add=False)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    adharno = models.PositiveIntegerField()
    mobileno = models.PositiveIntegerField()
    # student_id = models.CharField(max_length = 40)
    

    def __str__(self):
        return '%s' % (self.rollno)

class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    sname = models.CharField(max_length = 70)
    classes = models.CharField(max_length = 30)
    division = models.CharField(max_length = 30)
    # rollno = models.ForeignKey(Admission,related_name='rollno_Student_set', on_delete=models.CASCADE)
    rollno = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    taluka = models.CharField(max_length = 30)
    district = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    pincode = models.PositiveIntegerField()
    

class Marks(models.Model):
    sname = models.CharField(max_length = 70)
    classes = models.CharField(max_length = 30)
    division = models.CharField(max_length = 30)
    rollno = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)
    mark = models.CharField(max_length = 50)
    year = models.CharField(max_length = 10)

# class Collect(models.Model):
#     name = models.CharField(max_length = 70)
#     email = modelsCharField(max_length=70)
#     age = models.CharField(max_length=40)
#     phone = models.CharField(max_length=40)
#     amount = models.CharField(max_length=100)
#     # regno = models.CharField(max_length=100)
#     order_id = models.CharField(max_length=100,blank=True)
#     # razorpay_payment_id = models.CharField(max_length=100,blank=True)
#     paid = models.BooleanField(default=False)

 
# class User(models.Model):
#     name = models.CharField(max_length=70)
#     email = models.CharField(max_length=70)
#     pass1 = models.CharField(max_length=20)
    


    
           
 





