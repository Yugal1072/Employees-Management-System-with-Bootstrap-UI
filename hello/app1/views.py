from django.shortcuts import render
# Create your views here.

def home(request):
    
    employees = [
        {'name': 'yugal govind','age':26},
        {'name': 'aman dhole','age':18},
        {'name': 'ronit govind','age':29},
        {'name': 'sunita govind','age':48},
    ]
    for employee in employees:
        return render(request, 'index.html',context={'employees':employees, 'page': 'Home'})

def about(request):
    context = {'page': "About"}
    return render(request, 'about.html', context)
    
def contact(request):
    context = {'page': "Contact"}
     
    return render(request, 'contact.html', context)

def blog(request):
    context = {'page': "Blog"}
     
    return render(request, 'blog.html', context)