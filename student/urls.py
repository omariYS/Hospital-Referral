from django.urls import path
from .views import home_page

urlpatterns = [
    path("", home_page, name="home_page"), #This links the home.html file to django homepage
]