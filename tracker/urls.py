from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stateCon', views.stateCon, name='stateCon'),
    path('stateCured',views.stateCured,name ='stateCur'),
    path('stateDec',views.stateDec,name='stateDec'),
    path('contact', views.contact, name='contact'),
    path('<str:slug>', views.error, name='error'),
]
