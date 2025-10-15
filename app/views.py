from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':1222,'b':3456}
    return render(request,'conditions.html',d)