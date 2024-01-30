from django.contrib import admin
from newapp.models import  Student,Admission,Marks

# Register your models here.
class student_admin(admin.ModelAdmin):
    
    list_display=('sname','classes','division','rollno','address','taluka','district','state','pincode')
admin.site.register(Student,student_admin) 

class Admission_admin(admin.ModelAdmin):
    list_display=('sname','rollno','classes','mothername','gender','grno','religion','doa','dob','adharno','mobileno')
admin.site.register(Admission,Admission_admin)

class marks_admin(admin.ModelAdmin):
    list_display=('sname','classes','division','rollno','subject','mark','year')
admin.site.register(Marks,marks_admin)

# class Collect_admin(admin.ModelAdmin):
#     list_display=('sname','amount','regno','order_id','razorpay_payment_id','paid')
# admin.site.register(Collect,Collect_admin)


# class user_admin(admin.ModelAdmin):
#     list_display=('name','email','pass1')
# admin.site.register(User,user_admin)

