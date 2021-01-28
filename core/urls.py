
from django.urls import path
from .views import index, download

app_name = 'core'

urlpatterns = [
    path('', index),
    path('download/', download)
]
