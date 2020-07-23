from django.urls import path
from Social import views

app_name = "Social"

urlpatterns = [
    path('home/',views.home,name='home'),

]
