from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from .models import *
from django import template




def home(request):
    return render(request, "Management/Home.html",)

def Dashboard_customer(request):
    return render(request, "CustomerView/Dashboard_customer.html",)

def Dashboard_Staff(request):
    total_orders = len(Order.objects.all())
    total_reservations = len(Reservation.objects.all()) 
    total_customer = len(Customer.objects.all())
    return render(request, "Management/index.html",{"total_orders":total_orders,"total_reservations":total_reservations,"total_customer":total_customer})

def AboutUs(request):
    return render(request, "Management/AboutUs.html",)

def login_request(request):
    data = request.GET.get("data")
    print(data)
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        # try:
        #     user = Staff.objects.get(email=username,password=password)
        # except IntegrityError:
        #     return render(request, "Management/login.html", {
        #         "message": "Invalid username and/or password."
        #         })
            
        
        
        
        print(user)

        # Check if authentication successful
        if user is not None:
            
            if data=="staff":
                if user.is_staff == True:
                    login(request, user)
                    return HttpResponseRedirect(reverse("Dashboard_Staff"))
                else:
                    return render(request, "Management/login.html", {
                    "message": "You are not a Staff Member"
                    })
                
            elif data=="customer":
                if user.is_staff == False or user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect(reverse("Dashboard_customer"))
                else:
                    return render(request, "CustomerView/login.html", {
                    "message": " You Cannot use a staff Id to login to Customer interface"
                    })
                
        else:
            if data =="staff":
                return render(request, "Management/login.html", {
                "message": "Invalid username and/or password."
                })
    
            else:
                return render(request, 'CustomerView/login.html',{
                "message": "Invalid username and/or password."
                })
                    
    if data =="staff":
        return render(request, 'Management/login.html',)
    
    else:
        return render(request, 'CustomerView/login.html',)
        






def register(request):
    data = request.GET.get("data")
    print(data)
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        dob = request.POST["dob"]
        PNO = int(request.POST["phone_number"])
        address = request.POST["address"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = Staff.objects.create_user(email = email, user_name=username, first_name=username, password =password)
            user.save()
            # print(user)
            # print("its here........................")
            if data == "staff":
                salary= int(request.POST["salary"])
                designation=request.POST["designation"]
                user.salary= salary
                user.designation = designation
                user.dob = dob
                user.is_staff = True
                user.save()
                ph = Staff_phoneNo(staff=user,phone_number  = PNO)
                login(request, user)
                return render(request, "Management/index.html",)
            elif data == "customer":
                pass
                

        except IntegrityError:
            if data =="staff":
                return render(request, "Management/register.html", {
                "message": "Username already taken."
                })
    
            else:
                return render(request, 'CustomerView/register.html',{
                "message": "Username already taken."
                })
    else:
        if data =="staff":
            return render(request, 'Management/register.html',)
    
        else:
            return render(request, 'CustomerView/register.html',)



    
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def MS(request):
    return render(request, "Management/ManagementServices.html")

def show_order(request):
    # orders = Order.objects.get(id = 'UG901')
    # # for order in orders:
    # print(orders)
    # transactions = Transaction.objects.get(order=orders.id)
    # # for t in transactions:
    # print(transactions)
        
    # placed = PlaceOrder.objects.get(order=orders.id)
    # # for p in placed:
    # print(placed)
    # delivery = Delivery.objects.get(order=orders.id)
    # print(delivery)
    
    orders = Order.objects.all()
    # for order in orders:
    #     print(order)
    transactions = Transaction.objects.all()
    # for t in transactions:
    #     print(t)
        
    placed = PlaceOrder.objects.all()
    # makeTransc()
    
    return render(request,"Management/orders.html",{"orders":orders,"placed":placed,"transactions":transactions})

def team(request):
    data = request.GET.get('data')
    staff_mem = Staff.objects.filter(designation=data)
    phonenumber = []
    for s in staff_mem:
        phonenumber.append(Staff_phoneNo.objects.filter(staff = s.id).first())
        
    return render(request,"Management/team.html",{"data":data,"staff_mem":staff_mem,"phonenumber":phonenumber,})

def check_order(request,id):
    order = Order.objects.get(id=id)
    # try:
    #     customer_id = PlaceOrder.objects.get(order = id).customer
    #     ph = Customer_phoneNo.objects.get(customer = customer_id ).phone_number
    # except Customer_phoneNo.DoesNotExist:
    #     ph = None
    menu_orders = Order_Menu.objects.filter(order=id)
    # print(id)
    # print(order)
    # print(menu_order[0])
    
    return render(request,"Management/sp_order.html",{"id":id,"order":order,"menu_orders":menu_orders,})


def fire(request,user_name):
    print(user_name)
    user = Staff.objects.get(user_name=user_name)
    user.delete()
    return HttpResponseRedirect(reverse("MS"))

def DeliveryDone(request,id):
    data = request.GET.get('data')
    print(id)
    d = Delivery.objects.get(order=id)
        
    if data=="Done":
        d.status = "Completed"
    elif data == "Cancel":
        d.status = "Cancelled"
    d.save()
    return HttpResponseRedirect(reverse("order"))

def makeTransc():
    l = ["463","757","694","777","791","99","204","813","945"]

    menus = Menu.objects.all()
    orders = Order.objects.all()
    for order in orders:
        i = int(0)
        custid = l[i]
        i = i + int(1)
        price = 0
        status = "Due"
        menu_orders = Order_Menu.objects.filter(order=order.id)
        for m in menu_orders:
            price = price + m.menu.price * m.menu.timesOrdered;
        discount = 0.04*price
        tax	= 0.1*price
        amount_paid	= tax + price - discount
        customer = Customer.objects.get(id = custid)
        t = Transaction(order = order,customer=customer,price=price,amount_paid=amount_paid,tax=tax,discount=discount,status=status)
        t.save()
        
    return HttpResponseRedirect(reverse("order"))
        
    
        


    
    
    



 
 
# def export(request):
#     member_resource = CustomerResource()
#     dataset = member_resource.export()
#     #response = HttpResponse(dataset.csv, content_type='text/csv')
#     #response['Content-Disposition'] = 'attachment; filename="member.csv"'
#     #response = HttpResponse(dataset.json, content_type='application/json')
#     #response['Content-Disposition'] = 'attachment; filename="persons.json"'
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response
    