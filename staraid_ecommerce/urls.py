"""staraid_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from accounts import urls as urls_accounts
from django.conf.urls import url, include
from django.views import static
from .settings import MEDIA_ROOT
from home import views
from products import urls as urls_products
from products.views import all_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from search import urls as urls_search
from shipping import urls as urls_shipping
from home.urls import urlpatterns as index_pats
from newsletter.urls import urls as urls_newsletter

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include(urls_accounts)),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^products/', include(urls_products)),
    re_path(r'^cart/', include(urls_cart)),
    re_path(r'^search/', include(urls_search)),
    re_path(r'^checkout/', include(urls_checkout)),
    re_path(r'^shipping/', include(urls_shipping)),
    re_path(r'^newsletter/', include(urls_newsletter)),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^reviews/', include('reviews.urls')),
    re_path(r'',include(index_pats)),
]
