from django.urls import path
from .views import nested_view

urlpatterns = [
    path('', nested_view, name='nested_view'),
]