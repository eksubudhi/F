from django.urls import path
from Fibonacci_App import views

urlpatterns = [
    path('index', views.Fibonacci),
    path('Fibonacci1',views.Fibonacci1),

]
