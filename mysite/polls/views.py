from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello")

def page_top(request):
    return render(request, 'polls/page_top.html',{})

def page_menu(request):
    return render(request, 'polls/page_menu01.html')