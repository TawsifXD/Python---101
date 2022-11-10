from django.contrib import admin
from django.urls import path

from users.views import hello, goodbye, tawsif

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('goodbye/', goodbye),
    path('twasif/', tawsif),
]
