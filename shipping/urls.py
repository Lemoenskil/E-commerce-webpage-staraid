from django.conf.urls import url
from .views import adjust_region

urlpatterns = [
    url(r'^adjust_region/', adjust_region, name='adjust_region'),
]