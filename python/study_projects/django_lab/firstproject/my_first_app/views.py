from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
def hello_world(request, name):
    response = HttpResponse(f"<h1>Hello, {name}!</h1>")
    response.set_cookie('username', name)
    return response

def show_cookies(request):
    cookies = request.COOKIES
    return JsonResponse(cookies)

def redirect_example(request):
    return redirect('hello_world', name = "guest")

def json_example(request):
    user_data = {"name": "alex", "age": 25}
    return JsonResponse(user_data)