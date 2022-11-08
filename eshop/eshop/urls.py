"""eshop URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view as get_schema_view2
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Shop API')
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view2(
   openapi.Info(
      title="Shop API",
      default_version='v1',
      description="A Django API to build E-commerce",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('swagger/', schema_view),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/', obtain_auth_token),
    path('products/', include('products.urls')),
    path('category/', include('category.urls')),
    path('order/', include('order.urls')),
    path('cart/', include('cart.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)