from django.contrib import admin
from django.urls import path
from core.views import login,getData,register,postData


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/register', register),
    path('api/getData', getData),
    path('api/postData', postData),
]