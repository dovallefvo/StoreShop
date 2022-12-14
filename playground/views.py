from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to playground page.")
    
def sayHello(request):
    return HttpResponse("Hello world! :-D")
    
def showHelloPage(request):
    x = 1
    y = 2
    return render(request, 'hello.html')
