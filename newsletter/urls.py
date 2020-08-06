from .views import newsletter_subscribe
from django.urls import path, re_path


urls = [
    re_path(r'subscribe/', newsletter_subscribe, name='newsletter_subscribe'),
]
