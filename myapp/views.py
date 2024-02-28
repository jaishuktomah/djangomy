from django.shortcuts import render
from django.http import HttpResponse
from .models import ClassRoom
# Create your views here.
def home(request):
    return HttpResponse("""
     <html>
     <head>
     <title>myproject</title>
     </head>
     <body>
     <h1>Hello I am learning Django</h1>
     </body>
     </html>""")
    
    
def root_page(request):
    return render(request, template_name="myapp/root_page.html")    
              
def temp_inherit_home(request):
    return render(request, template_name="myapp/temp_inherit_home.html")  

def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")  

def classroom(request):
    classrooms = [
        {"name":"one", "address":"ktm"},
        {"name":"two", "address":"km"},
        {"name":"three", "address":"skt"}
    ]
    return render(request, template_name="myapp/classroom.html", 
                  context={"classroom_name":"one","location":"ktm","classrooms":classrooms}) 
    
def classroom_qs(request):
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="myapp/classroom_qs.html", 
                  context={"classrooms":classrooms})
    
    
    
    
    
