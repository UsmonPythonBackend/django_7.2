from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='products-list'),
    path('product/create/', ProductCreateView.as_view(), name='products-create'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]