from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'api'
urlpatterns = [
    path('get_ai_message', csrf_exempt(views.get_ai_message), name='get_ai_message')
]
