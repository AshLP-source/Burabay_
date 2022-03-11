import re
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Requests


def req(request):

    if request.method == 'GET':
        try:
            print(request.GET)
            requ = Requests()
            requ.name = request.GET['name']
            requ.phone_number = request.GET['number']
            requ.hotel = request.GET['hotel']
            requ.child = int(request.GET['child'])
            requ.adult = int(request.GET['adult'])
            requ.date1 = request.GET['date_in']
            requ.date2 = request.GET['date_out']
            response = ''
            if requ.hotel == 'RIXOS':
                response = 'https://www.rixos.com/ru/hotel-resort/rixos-borovoe'
            elif requ.hotel == 'Bereke':
                response = 'https://bereke-hotel-shchuchinsk.nochi.com/'
            elif requ.hotel == 'Sultan Plaza':
                response = 'https://sultanplaza.com/'
            elif requ.hotel == 'Green Which':
                response = 'http://greenwhich.kz/'
            print(requ)
            requ.save()
            return render(request,response)
        except Exception as e:
            print(str(e))
    else:
        print("DCDC")
    return render(request, 'index.html')


def home(request):
    if request.method == 'GET':
        req(request)
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def rooms(request):
    return render(request, 'rooms.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def single_blog(request):
    return render(request, 'single-blog.html')
