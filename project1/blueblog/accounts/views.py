from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("<h1>This is my first page</h1>")

def date_time(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    if h<12:
        msg="Hello everyone...! this is good morning time"
    elif h<16:
        msg="Hello everyone...! this is good afternoon time"
    elif h<21:
        msg="Hello everyone...! this is good evening time"
    else:
        msg="Hello everyone...! this is good night time"

    #dictionary
    my_dict={'date':date,"msg":msg}

    return render(request,'accounts/home.html',my_dict)
