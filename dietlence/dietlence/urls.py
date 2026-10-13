"""
URL configuration for dietlence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from diet_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',SignupView.as_view()),
    path('token',obtain_auth_token),
    path('profile/',ProfileView.as_view()),
    path('view/<int:pk>',ProfileRetriveView.as_view()),
    path('user/<int:pk>',UserRetriveView.as_view()),

    path('foodlog/',FoodLogCreateView.as_view()),
    path('retrive/<int:pk>',FoodLogRetriveView.as_view()),
    path('update/<int:pk>',FoodLogUpdateView.as_view()),
    path('delete/<int:pk>',FoodLogDeleteView.as_view()),
]
