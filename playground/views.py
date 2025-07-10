from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, world! This is the playground app.")


def testLife(request):
    return HttpResponse("This is a TestLife we have in a background.")

def say_hi(request):
    return render(request, 'hello.html',{'name': 'NatFlk', 'age': 20, 'hobby': ''})