from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# function home(req,res)
def home(request):
    return HttpResponse('<h1>My First Django Route!</h1>')

def about(request):
    return HttpResponse('<h1>About the CatCollector</h1>')

def contact(request):
    return HttpResponse('<h1>Conttact Pagepy</h1>')
