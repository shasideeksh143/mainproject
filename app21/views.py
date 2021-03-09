from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import StudentModel,LoginModel

# Create your views here.
def index(request):
    return render(request,'home.html')
def stulogin(request):
    return render(request,'login.html')
def sturegistration(request):
    return render(request,'regiser.html')


def forgottenPassword(request):
    return render(request,'forgottenpassword.html')

#here iam getting registratio form detailes
def storeinModel(request):
    na=request.POST.get('t1')
    age = request.POST.get('t2')
    con = request.POST.get('t3')
    gen = request.POST.get('t4')
    uname = request.POST.get('t5')
    pw=request.POST.get('t6')
    type='student'
    # here iam svaving all detailes in studentmodel except password and type

    data1=StudentModel(name=na,age=age,gender=gen,contactno=con,username=uname)
    data1.save()
    # here iam svaving username and password and type in loginmodel
    data2=LoginModel(username=uname,password=pw,type=type)
    data2.save()
    messages.success(request,'thanks for registration')
    return redirect('stu_registration')



# here iam checking username and password by getting detalies from login form
def stucheck(request):
    uname=request.POST.get('uname')
    pw = request.POST.get('pw')
    type='student'
    try:
       LoginModel.objects.get(username=uname,password=pw,type=type)
       print('ok')
       return render(request,'stu_welcomehome.html',{'name':uname})
    except LoginModel.DoesNotExist:
        messages.error(request,'invalid user')
        return redirect('stu_login')

def stuhome(request):
    uname=request.GET.get('un')
    print(uname)
    return render(request,'stu_welcomehome.html',{'name':uname})

def view_stuprofile(request):
    uname=request.GET.get('un')
    print(uname)
    data=StudentModel.objects.get(username=uname)
    return render(request,'viewstu_profile.html',{'name':uname,'data':data})

def update_stuprofile(request):
    uname = request.GET.get('un')
    data = StudentModel.objects.get(username=uname)
    return render(request,'updatestu_profile.html',{'name':uname,'data':data})


def adminlogin(request):
    return render(request,'admin_login.html')


def admincheck(request):
    un=request.POST.get('uname')
    pw=request.POST.get('pw')
    type='admin'
    try:
      LoginModel.objects.get(username=un,password=pw,type=type)
      return render(request,'adminwelcomehome.html',{'name':un})
    except LoginModel.DoesNotExist:
        messages.error(request,'Invalid Admin Detailes')
        return redirect('admin_login')

def adminhome(request):
    uname=request.GET.get('un')
    return render(request,'adminwelcomehome.html',{'name':uname})


def doupdate(request):
    name=request.POST.get('un')
    age = request.POST.get('ua')
    gen = request.POST.get('ug')
    con = request.POST.get('uc')
    uname = request.POST.get('uu')
    try:
       StudentModel.objects.filter(username=uname).update(name=name,age=age,gender=gen,contactno=con)
       data=StudentModel.objects.get(username=uname)
       return render(request,'viewstu_profile.html',{'name':uname,'data':data})
    except:
        data = StudentModel.objects.get(username=uname)
        return render(request,'updatestu_profile.html',{'name':uname,'data':data,'message':'Uniq Constraints cannot modified'})


def showpw(request):
    uname=request.POST.get('un')
    con=request.POST.get('con')
    try:
        StudentModel.objects.get(username=uname,contactno=con)
        pw=LoginModel.objects.get(username=uname)
        return render(request, 'forgottenpassword.html', {'pw': pw})
    except :
        return render(request,'forgottenpassword.html',{'message':'Invalid Details'})


def viewallstudents(request):
    uname=request.GET.get('un')
    data=StudentModel.objects.all()
    print(type(data))
    return render(request,'view_allstudents.html',{'name':uname,'data':data})

def deletestudent(request):
    uname=request.GET.get('un')
    data = StudentModel.objects.all()
    return render(request,'delete_student.html',{'name':uname,'data':data})


def dodelete(request):
    uname=request.GET.get('un')
    un1 = request.GET.get('un1')
    StudentModel.objects.filter(username=uname).delete()
    LoginModel.objects.filter(username=uname).delete()
    data=StudentModel.objects.all()
    return render(request,'delete_student.html',{'name':un1,'data':data})



