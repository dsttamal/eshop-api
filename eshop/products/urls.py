from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.get_products.as_view()),
    path('<int:id>/', views.get_product_by_id.as_view()),
    path('<str:type>/<str:slug>/', views.get_product_by_category_subCategory_Vendor.as_view()),
]
