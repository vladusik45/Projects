from django.urls import path
from my_first_app.views import hello_world, json_example, redirect_example, show_cookies

urlpatterns = [
    path('redirect/', redirect_example, name='redirect_example'),
    path('json/', json_example, name='json_example'),
    path('cookies/', show_cookies, name='show_cookies'),
    path('<str:name>/', hello_world, name='hello_world'),
]
