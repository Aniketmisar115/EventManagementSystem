
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello,")
def home(request):
    return HttpResponse("****Welcome To My Page****")
def about(request):
    name="Saloni"
    events= [
        {
        "name":"Freshers",
        "organiser":"NAAC commitiee ",
        "special_guest":"Secretary Of JCOET ",
        "date"  :"20/04/2022 ",
        "venue" :"At sir vishveshwaraya hall "
        },
        {
        "name":"Farewell",
        "organiser":"computer Dept",
        "special_guest":"Principal Of JCOET",
        "date"  :"21/04/2022",
        "venue" :"At sir Bhatkar hall"
        },
    
    ]
    context={"display_name":name,"event_details":events}
    return render(request,"event_handling.html",context)
    #return HttpResponse("This is event handling page")
