from django.urls import re_path, include
from .views import checkout

urlpatterns = [
    re_path(r'^$', checkout, name='checkout'),
]