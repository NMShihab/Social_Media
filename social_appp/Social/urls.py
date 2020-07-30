from django.urls import path
from Social import views

app_name = "Social"

urlpatterns = [
    path('home/',views.home,name='home'),
    path('liked/<pk>',views.liked_post,name='liked'),
    path('unliked/<pk>',views.unliked_post,name='unliked')

]
