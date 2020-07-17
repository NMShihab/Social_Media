from django.urls import path
from Login import views

app_name = "Login"

urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
]
