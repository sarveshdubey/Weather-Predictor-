from django.urls import path 
from api import views
from .views import post, export,result

urlpatterns=[
    path('',views.post,name="Post"),
    path('ex',views.export,name="Export"),
    path('result',views.result,name="result")
]