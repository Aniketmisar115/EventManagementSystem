from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,")
def home(request):
    return HttpResponse("****Welcome To My Page****")
def about(request):
    return HttpResponse("This is event handling page")