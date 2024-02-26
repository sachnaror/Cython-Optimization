from cpyApp import fib  # Import the missing module
from django.http import HttpResponse  # Import the missing module
from django.shortcuts import render

# Create your views here.


def heavy_computation(request):
    result = fib(10)  # Just an example; replace 10 with your desired input
    return HttpResponse(f"The result is {result}")
