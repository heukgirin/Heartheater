from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Listing
import requests

def index(request):
    item_list = Listing.objects.all()
    context = {'item_list' : item_list}
    return render(request, 'items/index.html', context)

def list(request):
    item_list = Listing.objects.all()
    curr_page = "a"
    context = {'item_list' : item_list , 'curr_page' : curr_page}
    return render(request, 'items/list.html', context)

def count(request):
    with requests.Session() as s:
        # HTTP GET Request: requests대신 s 객체를 사용한다.
        req = s.get('http://112.175.234.157/COWELL/')
        # HTML 소스 가져오기
        html = req.text
        # HTTP Header 가져오기
        header = req.headers
        # HTTP Status 가져오기 (200: 정상)
        status = req.status_code
        # HTTP가 정상적으로 되었는지 (True/False)
        is_ok = req.ok

    return render(request, 'items/list.html', is_ok)
