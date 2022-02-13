from django.urls import path
from .views import welcome , products

urlpatterns = [
    path("welcome/", welcome),
    path("products/", products),

]
