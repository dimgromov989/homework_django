from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product


def contacts(request):
    """Контроллер для страницы контактов с post-запросом"""
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f'Спасибо, {name}! Сообщение получено, вот его текст: "{message}".'
        )
    return render(request, "contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
