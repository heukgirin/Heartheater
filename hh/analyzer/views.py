from django.shortcuts import render
from django.http import HttpResponse
from parts.excel import ExcelCon

def index(request):
    context = {'context' : 'test'}
    return render(request, 'index.html', context)
