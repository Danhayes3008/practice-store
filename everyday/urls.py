"""everyday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users.views import index
from basket import urls as urls_basket
from users import urls as urls_users
from stock import urls as urls_stock
from stock.views import products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', products, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(urls_users)),
    url(r'^stock/', include(urls_stock)),
    url(r'^basket/', include(urls_basket)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
