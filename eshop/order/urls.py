from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.get_order_by_user.as_view()),
    path('add/', views.add_order.as_view()),
    path('<int:id>/', views.get_order_by_id.as_view()),
]
