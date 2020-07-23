
from django.contrib import admin
from django.urls import path, include
from Social import views

# For media Profile
from django.conf import settings
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Login.urls')),
    path('post/', include('Social.urls')),
    path('',views.home,name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
