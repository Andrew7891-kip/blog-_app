from django.urls import path 
from . import views

urlpatterns = [
    path('',views.post,name='post'),
    path('<int:pk>',views.post_detail,name='post_detail'),
    path('<int:pk>',views.post_form,name='post_form'),
]