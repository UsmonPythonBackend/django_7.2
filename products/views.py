from django.shortcuts import render, redirect
from django.views import View
from products.forms import ProductForm
from products.models import Product
from django.views.generic import ListView, DetailView
from django.contrib import messages



# Create your views here.
# class ProductsView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         context = {'products': products}
#         return render(request, "shop.html", context)

class ProductListView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = "products"

class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, "shop-detail.html", {"product": product})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "product_create.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = product.title + "001"
            product.save()
            return redirect("products-list")

