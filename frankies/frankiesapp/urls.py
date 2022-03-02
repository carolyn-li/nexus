"""frankies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_world, name='hello_world'),
    path('add_product', views.add_product, name='add_product'),
    path('add_productcollection', views.add_productcollection, name='add_productcollection'),
    path('remove_productcollection/<int:pk>', views.delete_productcollection, name='delete_productcollection'),
    path('update_productcollection/<int:pk>', views.update_productcollection, name='update_productcollection'),
    path('view_products', views.view_products, name='view_products'),
    path('adminview_products', views.view_product, name="view_products")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)