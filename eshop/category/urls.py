from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.get_category.as_view()),
    path('sub_category/', views.get_sub_category.as_view()),
    path('vendor/', views.get_vendor.as_view()),
    
]
