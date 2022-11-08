from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.get_cart.as_view()),
    path('<int:id>/', views.get_cart_by_id.as_view()),
    path('add/', views.add_to_cart.as_view()),
    path('delete/<int:id>/', views.delete_cart_data.as_view()),
]
