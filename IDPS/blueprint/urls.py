from django.urls import path
from . import views
urlpatterns=[
    path('',views.test),
    path('demo',views.demo),
    path('love',views.love),
    path('factorial',views.factorial),
    path('demoo',views.demoo),
   
]