from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Контроллер для главной страницы"""
    return render(request, "home.html")


def contacts(request):
    """Контроллер для страницы контактов с post-запросом"""
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f'Спасибо, {name}! Сообщение получено, вот его текст: "{message}".'
        )
    return render(request, "contacts.html")
