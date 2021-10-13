from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('result',views.index2),
    path('redirect',views.index3),
]