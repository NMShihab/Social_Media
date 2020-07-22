from django.urls import path
from Login import views

app_name = "Login"

urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.Login_page,name='login'),
    path('edit/',views.edit_profile,name='edit'),
    
]
