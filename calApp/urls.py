from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('delete/ <int:id>/',delete,name='delete'),
    path('create/',create,name='create'),
    path('data/',data,name='data'),
]
 