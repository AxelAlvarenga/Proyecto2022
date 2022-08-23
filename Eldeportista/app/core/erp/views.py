from django.shortcuts import render

# Create your views here.

def vista1(request):
    data={
            "name":"axel"    

        }
    return render(request,'templates/home.html',data)
