from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from newapp.models import  Student,Admission,Marks
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.conf import settings
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO



# import pdfkit
# config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
# Create your views here.

def signupPage(request):
    if request.method=='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(pass1!=pass2):
            return HttpResponse('Password Not Matched')
        else:
            my_user=User.objects.create_user(name,email,pass1)
            my_user.save() 
           
            return redirect('login')

    return render(request,'signup.html')

def loginPage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password Incorrect")

    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')
           

@login_required(login_url='login') 
@csrf_exempt      
def home(request):
    return render(request,'homepage.html')

@login_required(login_url='login') 
def student(request):
    # try:
        if request.method == "POST":
           sname = request.POST.get('sname')
           classes = request.POST.get('classes')
           division = request.POST.get('division')
           rollno = request.POST.get('rollno')
           address = request.POST.get('address')
           taluka = request.POST.get('taluka')
           district = request.POST.get('district')
           state = request.POST.get('state')
           pincode = request.POST.get('pincode')
           en=Student(sname=sname,classes=classes,division=division,rollno=rollno,address=address,taluka=taluka,district=district,state=state,pincode=pincode)
           en.save()
        # Student.objects.create(sname=sname,regno=regno,address=address,taluka=taluka,district=district,state=state,pincode=pincode)

           return  redirect('stu')
    # except:
    #     return HttpResponse("You are Not Registered")
    # render(request,"student.html")
    
        return render(request,"student.html")


# @login_required(login_url='login')
def bd(request):
    if request.method == "POST":
        sname = request.POST.get('sname')
        classes = request.POST.get('class')

        request.session['bonafide_data'] = {
            'sname' : sname,
            'classes' : classes,
        }

        return redirect('bonafide')
    
    return render(request,"bd.html")

# @login_required(login_url='login') 
def bonafide(request):
    
    bonafide_data = request.session.get('bonafide_data', {})
    sname = bonafide_data.get('sname')
    classes = bonafide_data.get('classes')

    data1 = get_object_or_404(Admission, sname=sname)

    data2 = Student.objects.get(classes=classes)

    context = {'sname' : data1.sname,
               'address' : data2.address,
               'taluka' : data2.taluka,
               'district' : data2.district,
               'class' : data1.classes,
               'dob' : data1.dob,
               'gr' : data1.grno,
               'doa' : data1.doa,
               }

    return render(request,"bonafide.html",context)

@login_required(login_url='login') 
def admission(request):
    
    if request.method == "POST":
        sname = request.POST.get('sname')
        rollno = request.POST.get('rollno')
        classes = request.POST.get('classes')
        mothername = request.POST.get('mothername')
        gender = request.POST.get('gender')
        grno= request.POST.get('grno')
        religion = request.POST.get('religion')
        doa = request.POST.get('doa')
        dob = request.POST.get('dob')
        adharno = request.POST.get('adharno')
        mobileno = request.POST.get('mobileno')
        # student_id = request.POST.get('studentid')

        en=Admission(sname=sname,rollno=rollno,classes=classes,mothername=mothername,gender=gender,grno=grno,religion=religion,
                     doa=doa,dob=dob,adharno=adharno,mobileno=mobileno)
        en.save()
        # Admission.objects.create(regno=regno,sname=sname,classes=classes,branch=branch,doa=doa,semester=semester
    return render(request,"admission.html")

@login_required(login_url='login') 
def marks(request):
    dict={}
    if request.method == "POST":
        sname = request.POST.get('sname')
        classes = request.POST.get('classes')
        division = request.POST.get('division')
        rollno = request.POST.get('rollno')
        subject = request.POST.get('subject')
        mark = request.POST.get('mark')
        year = request.POST.get('year')
        en=Marks(sname=sname,classes=classes,division=division,rollno=rollno,subject=subject,mark=mark,year=year)
        en.save()
        # Marks.objects.all(user=user,regno=regno,subject=subject,mark=mark,semester=semester,year=year)
    
    return render(request,"marks.html")
        
@login_required(login_url='login') 
def feedback(request):
    context={}
    adm = Student.objects.all()
    m = Marks.objects.all()
    a = Admission.objects.all()
    context = {'sdata': adm,
     'mdata': m,
     'adata': a
        }
    return render(request,"feedback.html",context)

@login_required(login_url='login') 
def search(request):
    context = {}
    adata = []
    mdata = []
    sdata = []
    if request.method == "POST":
       sname = request.POST.get('sname')
       rollno = request.POST.get('rollno')
       classes = request.POST.get('class')

       
       if sname:
            # Search in both Admission and Student models for sname
            adata += list(Admission.objects.filter(Q(sname__iexact=sname)))
            sdata += list(Student.objects.filter(Q(sname__iexact=sname)))
            mdata += list(Marks.objects.filter(Q(sname__iexact=sname)))
       if rollno:
            # Search in all three models for rollno
            if sname:
                adata += list(Admission.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno)))
                sdata += list(Student.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno)))
                mdata += list(Marks.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno)))
            else:
                adata += list(Admission.objects.filter(Q(rollno__iexact=rollno)))
                sdata += list(Student.objects.filter(Q(rollno__iexact=rollno)))
                mdata += list(Marks.objects.filter(Q(rollno__iexact=rollno)))
       if classes:
            if sname:
                if classes:
                    adata += list(Admission.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno,classes__iexact=classes)))
                    sdata += list(Student.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno,classes__iexact=classes)))
                    mdata += list(Marks.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno,classes__iexact=classes)))
                
                if rollno:
                    adata += list(Admission.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno)))
                    sdata += list(Student.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno)))
                    mdata += list(Marks.objects.filter(Q(sname__iexact=sname,rollno__iexact=rollno)))
                

            else:
                adata += list(Admission.objects.filter(Q(classes__iexact=classes)))
                sdata += list(Student.objects.filter(Q(classes__iexact=classes)))
                mdata += list(Marks.objects.filter(Q(classes__iexact=classes)))
           
        

       context = {
        "adata":adata,
        "sdata":sdata,
        "mdata":mdata,
       }
       return render(request,'feedback.html',context)

  # elif request.method == 'GET':              this can be written or not
    return render(request,'search.html')


# def show(request):
#     bonafide_data = request.session.get('bonafide_data', {})
#     sname = bonafide_data.get('sname')
#     classes = bonafide_data.get('classes')

#     data1 = get_object_or_404(Admission, sname=sname)

#     data2 = Student.objects.get(classes=classes)

#     context = {'sname' : data1.sname,
#                'address' : data2.address,
#                'taluka' : data2.taluka,
#                'district' : data2.district,
#                'class' : data1.classes,
#                'dob' : data1.dob,
#                'gr' : data1.grno,
#                'doa' : data1.doa,
#                }
#     return render(request,'show_pdf.html',context)




def bonafide_certificate(request):
    # Your certificate data goes here, you can pass it through the context


    bonafide_data = request.session.get('bonafide_data', {})
    sname = bonafide_data.get('sname')
    classes = bonafide_data.get('classes')

    data1 = get_object_or_404(Admission, sname=sname)

    data2 = Student.objects.get(classes=classes)

    context = {'sname' : data1.sname,
               'address' : data2.address,
               'taluka' : data2.taluka,
               'district' : data2.district,
               'class' : data1.classes,
               'dob' : data1.dob,
               'gr' : data1.grno,
               'doa' : data1.doa,
               }
    
    template_path = 'bonafide.html'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Bonafide.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html,dest=response
    )

    if pisa_status.err:
        return HttpResponse('Their were some errors <pre>' + html + '</pre>')
    
    return response