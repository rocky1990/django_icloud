from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def xianshihanshu(request):
    return HttpResponse("hello")
def xianshipingtai(request):
    return render(request, 'platform.html')