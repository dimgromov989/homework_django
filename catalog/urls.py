from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, product_detail, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name="products_list"),
    path("products/<int:pk>/",product_detail, name="product_detail"),

]
