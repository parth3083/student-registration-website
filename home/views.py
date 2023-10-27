from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact,Register,Usname,Password_Configuration
def index(request):
    context={
        "variable1":"This is sent by Parth",
        "variable2":"Parth is great."
    }
    return render(request,"index.html",context)
    # return HttpResponse("This is the home page")
def about(request):
    return render(request,"about.html")
    # return HttpResponse("This is the about page")
def service(request):
    return render(request,"services.html")
    # return HttpResponse("This is the service page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,"contact.html")
def forgot(request):
    if request.method=="POST":
        usname1=request.POST.get('usname1')
        op=request.POST.get('op')
        np=request.POST.get('np')
        p_c=Password_Configuration(usname1=usname1,op=op,np=np)
        p_c.save()
    return render(request,"forgot.html")
def register(request):
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        phone1=request.POST.get('phone')
        add=request.POST.get('add')
        password=request.POST.get('password')
        enrol=request.POST.get('numb')
        city=request.POST.get('city')
        pin=request.POST.get('pin')
        regis=Register(name1=name1,email1=email1,phone1=phone1,add=add,password=password,enrol=enrol,city=city,pin=pin,date=datetime.today())
        regis.save()
    return render(request,"register.html")
def upload(request):
    return render(request,"upload.html")
def sign(request):
    if request.method=="POST":
        usname=request.POST.get('usname')
        email2=request.POST.get('email')
        password1=request.POST.get('password')
        us=Usname(usname=usname,email2=email2,password1=password1,date=datetime.today())
        us.save()
    return render(request,"sign.html")
    # return HttpResponse("This is the contact page")
