from django.urls import path, include
from . import urls_reset
from .views import register, update, logout, login

urlpatterns = [
    path('register/', register, name='register'),
    path('update/', update, name='update'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('password-reset/', include(urls_reset)),
]