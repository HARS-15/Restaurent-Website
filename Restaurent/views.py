from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
def single_category(request):
    val=request.GET["menu_id"]
    category=Menu.objects.get(id=val)
    if category.name in ["IceCreams","Drinks","Meals"]:
        val=0
        items=Neutral.objects.filter(menu_category=category.name).order_by('price')
        return render(request,'single_category.html',{'items':items,'val':val,'category':category.name})
    else:
        val=1
        dest_veg=Veg_item.objects.filter(menu_category=category.name).order_by('price')
        dest_non_veg=Non_veg_item.objects.filter(menu_category=category.name).order_by('price')
        return render(request,'single_category.html',{'veg':dest_veg,'non_veg':dest_non_veg,'category':category.name,'val':val})
def menu(request):
    dest=Menu.objects.exclude(id=12).order_by('position')
    return render(request,'menu.html',{'dest':dest})
def main(request):
    return render(request,'main.html') 
def register(request):
    if request.method=='POST':
        f_name=request.POST['first_name']
        l_name=request.POST['last_name']
        u_name=request.POST['user_name']
        mail=request.POST['email_id']
        p1=request.POST['password']
        p2=request.POST['c_password']
        if p1==p2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,message="Username already exists!!")
                return redirect(register)
            elif User.objects.filter(email=mail).exists():
                messages.info(request,message="Email already used!!!")
                return redirect(register)
            else:
                user=User.objects.create_user(password=p1,first_name=f_name,last_name=l_name,email=mail,username=u_name)
                user.save()
                return redirect(login)

        else:
            messages.info(request,message="Passwords are not matched!!!")
            return redirect(register)
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        mail=request.POST['mail']
        password=request.POST['password']
        try:
            user=User.objects.get(email=mail)
            user1=auth.authenticate(username=user.username,password=password)
            if user1 is not None:
                auth.login(request,user1)
                return redirect("/")
            else:
                messages.info(request,message='Invalid User Credentials!!!')
                return render(request,"login.html")
        except:
            messages.info(request,message='Invalid User Credentials!!!')
            return render(request,"login.html")
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")