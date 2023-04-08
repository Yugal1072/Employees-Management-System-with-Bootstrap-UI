from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import Employees

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