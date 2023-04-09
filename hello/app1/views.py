from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import Employees
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    # title = {'page': "Home"}
    if request.method == "POST":
        data = request.POST
        
        name = data.get("name")
        age = data.get("age")
        email = data.get("email")
        address = data.get("address")
        photo = request.FILES.get('photo')

        Employees.objects.create(
            name = name,
            age = age,
            email = email,
            address = address,
            photo = photo,
            )
        return redirect('/')   

    query_set = Employees.objects.all()
    context = {'employees': query_set}

    return render(request, 'index.html', context)


def delete(request,id):
    queryset = Employees.objects.get(id = id)
    queryset.delete()
    return redirect("/")

def update(request,id):

    queryset = Employees.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        
        name = data.get("name")
        age = data.get("age")
        email = data.get("email")
        address = data.get("address")
        photo = request.FILES.get('photo')
        
        queryset.name = name
        queryset.age = age
        queryset.email = email
        queryset.address = address

        if photo:
           queryset.photo = photo
           
        queryset.save()
        return redirect("/")

    context = {'employees': queryset}
    return render(request,"update.html", context)

def about(request):
    context = {'page': "About"}
    return render(request, 'about.html', context)
    
def contact(request):
    context = {'page': "Contact"}
     
    return render(request, 'contact.html', context)

def blog(request):
    context = {'page': "Blog"}
     
    return render(request, 'blog.html', context)


def login_page(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid Username")
            return redirect("/login/")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")
        
        
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")

def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request,"Username Already Exist")
            return redirect("/register/")

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            )
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")

        return redirect("/register/")
    return render(request,"register.html")