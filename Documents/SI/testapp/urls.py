"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import testapp
from testapp import views


urlpatterns = [
    path('', views.home),
    path('accounts/login/', views.login),
    path('accounts/auth/', views.auth_view),
    path('accounts/loggedin/', views.loggedin),
    path('accounts/logout/', views.logout),
    path('eleve/create/', views.eleve_create),
    path('eleve/all/', views.eleve_list),
    path('groupe/create/', views.groupe_create),
    path('groupe/all/', views.groupe_list),
    path('groupe/classe/<int:id_groupe>/', views.eleve_groupe, name='classe_list'),

]
