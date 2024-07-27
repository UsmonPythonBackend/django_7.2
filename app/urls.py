from django.urls import path
from .views import ProductListView, ContactView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
