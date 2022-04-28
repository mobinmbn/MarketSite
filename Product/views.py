from django.shortcuts import render
from django.views.generic import TemplateView
from Product.models import Product


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class TeamView(TemplateView):
    template_name = "team.html"


class RequestDemoView(TemplateView):
    template_name = "request-demo.html"


class LoginView(TemplateView):
    template_name = "login.html"


def product_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'Product/product.html', context)


def product_single_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product": product
    }
    return render(request, 'Product/single_product.html', context)
