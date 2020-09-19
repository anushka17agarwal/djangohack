from django.shortcuts import render
import requests


def home(request):
    r = requests.get("http://gsx2json.com/api?id=1aLH0dQFW3mN5vSxJdhjdQuAMTKojCDn-7mk6CNH3W68&sheet=1")
    j=r.json()
    
    return render(request, 'app1/home.html', j)
