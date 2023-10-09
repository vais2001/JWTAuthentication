from django.contrib import admin
from django.urls import path,include
from jwtapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jwtapp.urls')),
]
