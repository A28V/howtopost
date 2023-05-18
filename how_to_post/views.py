from django.shortcuts import render
from django.http import HttpResponse;

def index(request):
    return render(request,'formpost.html')


def formdata(request):
    if request.method == "POST":
        name=request.POST.get('name')
        return render(request,'Details.html',{'name':name})
	      