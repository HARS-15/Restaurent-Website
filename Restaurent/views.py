from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def single_category(request,menu_id):
    menu=get_object_or_404(Menu, id=menu_id)
    if menu.name in ["Ice Creams","Drinks","Meals"]:
        val=0
        items=MenuItem.objects.filter(menu_category=menu.name,item_type="NE").order_by('price')
        return render(request,'single_category.html',{'items':items,'val':val,'category':menu.name,'menu_id':menu_id})
    else:
        val=1
        dest_veg=MenuItem.objects.filter(menu_category=menu.name,item_type="V").order_by('price')
        dest_non_veg=MenuItem.objects.filter(menu_category=menu.name,item_type="NV").order_by('price')
        return render(request,'single_category.html',{'veg':dest_veg,'non_veg':dest_non_veg,'category':menu.name,'menu_id':menu_id,"val":val})


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
    

def profile(request):
    order_items = request.session.get("order_items", {})
    item_ids=list(order_items.keys())
    current_items = MenuItem.objects.filter(id__in=item_ids)
    item_list = {item: order_items[str(item.id)] for item in current_items}
    orders=Orders.objects.filter(user=request.user).order_by("-created_at")
    return render(request,'profile.html',{"orders":orders,"current_items":item_list})


def login(request):
    if request.method=="POST":
        mail=request.POST['mail']
        password=request.POST['password']
        try:
            user=User.objects.get(email=mail)
            user1=auth.authenticate(username=user.username,password=password)
            if user1 is not None:
                auth.login(request,user1)
                create_new_order_list(request)
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
    if 'order_items' in request.session:
        del request.session["order_items"]
    return redirect("/")

def create_new_order_list(request):
     if 'order_items' in request.session:
        del request.session['order_items']

@login_required
def ordered_items(request):
    val=str(request.GET["item_id"])
    if "order_items" not in request.session:
        request.session["order_items"]={}
    order_items=request.session["order_items"]
    if val in order_items:
        order_items[val]+=1
    else:
        order_items[val]=1
    request.session["order_items"]=order_items
    request.session.modified=True
    menu_id=request.GET["menu_id"]
    return redirect("single_category",menu_id=menu_id)


@require_POST
def place_order(request):
    if "order_items" in request.session and request.session["order_items"]:
        updated_order_items = {}
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                item_id = key.split('_')[1]
                quantity = int(value)
                if quantity > 0:
                    updated_order_items[item_id] = quantity
        item_ids=list(updated_order_items.keys())
        current_items = MenuItem.objects.filter(id__in=item_ids)
        item_list = {item: updated_order_items[str(item.id)] for item in current_items}
        request.session["order_items"] = updated_order_items
        total= sum(item.price * quantity for item, quantity in item_list.items())
        return render(request,'order_page.html',{"current_items":item_list,"total":total})
    
def order(request):
    if "order_items" in request.session and request.session["order_items"]:
        order=Orders.objects.create(user=request.user)
        for item_id, quantity in request.session["order_items"].items():
            menu_item = MenuItem.objects.get(id=item_id)
            order_item = OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        item_ids=list(request.session["order_items"].keys())
        current_items = MenuItem.objects.filter(id__in=item_ids)
        item_list = {item: request.session["order_items"][str(item.id)] for item in current_items}
        order.Amount=sum(item.price * quantity for item, quantity in item_list.items())
        order.save()
        del request.session["order_items"]
        return redirect("/")
    
def remove(request):
    if "order_items" in request.session and request.session["order_items"]:
        val=request.GET['item_id']
        if val in request.session["order_items"]:
            del request.session["order_items"][val]
            request.session.modified = True
            request.session.save()
        return redirect(profile)