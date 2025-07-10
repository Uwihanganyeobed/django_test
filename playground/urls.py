from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.say_hello, name='say_hello'),
    path('testLife', views.testLife, name='test_life'),
    path('hey', views.say_hi, name='hey'),
]
