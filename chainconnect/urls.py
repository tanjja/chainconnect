"""
URL configuration for chainconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from core.views import index, cart, checkout, store, updateItem, confirm, processOrder

urlpatterns = [
    path('', index, name = 'index'),
    path('home/', index, name = 'index'),
    path('store/', store, name = 'store'),
    path('cart/', cart, name = 'cart'),
    path('checkout/', checkout, name = 'checkout'),
    path('admin/', admin.site.urls),
    path('confirm/', confirm, name = 'confirm'),

    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)