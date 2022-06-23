from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import sec


def home(request):
    return render(request, "home/index.html")

def Signup(request):
    if request.method =="POST":
       username = request.POST.get("username")
       email = request.POST.get("email")
       fname = request.POST.get("fname")
       lname = request.POST.get("lname")
       password1 = request.POST.get("password1")
       password2 = request.POST.get("password2")
        
       if password1 == password2:
            new_user = User.objects.create_user(username=username,
                                                email=email,
                                                first_name=fname,
                                                last_name=lname,
                                                password=password1)
            new_user.save()
            return redirect("home:login")
    return render(request, "home/manage_signup.html")





def login_view(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home:home")
    return render(request, "home/login.html")




def add_customer(request):
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        amount_paid = request.POST.get("amount_paid")
        occupants_name = request.POST.get("occupants_name")
        email = request.POST.get("email")
        occupants_occupation = request.POST.get("occupants_occupation")
        non = request.POST.get("NON")
        start_date = request.POST.get("start_date")
        end_date  = request.POST.get("end_date")
        
        new_customer = sec(room_number=room_number, amount_paid=amount_paid, occupants_name=occupants_name, occupants_email=email, occupants_occupation=occupants_occupation, number_of_nights=non, start_date=start_date, end_date=end_date)
        new_customer.save()
        return redirect("home:home")
    return render(request, "home/add_customer.html")


def logout_view(request):
    logout(request)
    return render(request, "home/logout.html")