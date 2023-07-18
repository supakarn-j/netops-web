from django.shortcuts import render
from django.http import HttpResponseRedirect
from sqlalchemy import ExecutableDDLElement
from config import settings
from schemas import service
import requests

# Create your views here.
def index(request):
    r = requests.get(settings.API_URL + '/services')
    services = list(map(lambda x: service.Service(**x),r.json()['data']))
    # print(services)
    # for i in services:
    #     print(i.id)
    return render(request, 'index.html', { "services": services })

def service_update(request, id):
    if request.method == "POST":
        req = request.POST
        print(req.dict())

        r = requests.put(settings.API_URL + '/services/' + str(id), json=req.dict())
        print(r.status_code)
        print(r.json())
    return HttpResponseRedirect('/')

def service_add(request):
    if request.method == "POST":
        req = request.POST
        print(req.dict())

        r = requests.post(settings.API_URL + '/services', json=req.dict())
        print(r.status_code)
        print(r.json())
    return HttpResponseRedirect('/')