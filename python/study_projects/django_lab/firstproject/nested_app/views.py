from django.shortcuts import render
from django.http import HttpResponse

def nested_view(request):
    return HttpResponse("<h1>Welcome to Nested App!</h1>")