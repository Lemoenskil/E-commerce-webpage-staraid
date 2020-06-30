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
from django.urls import path
from accounts import urls as urls_accounts
from django.conf.urls import url, include

print(admin.site.urls)
print(include(urls_accounts))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls_accounts)),
]

#  url(r'^admin/', admin.site.urls),
#     url(r'^$', all_products, name='index'),
#     url(r'^accounts/', include(urls_accounts)),
#     url(r'^products/', include(urls_products)),
#     url(r'^cart/', include(urls_cart)),
#     url(r'^checkout/', include(urls_checkout)),
#     url(r'^search/', include(urls_search)),
#     url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
# ]