from django.urls import path
from .views import email_view

app_name = 'vade'

urlpatterns = [
    path('', email_view, name='sendmail')
]
