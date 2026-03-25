from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Product


class ContactsView(ListView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object




class ProductCreateView(CreateView):
    model = Product
    fields  = ['name', 'image', 'category', 'purchase_price']
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields  = ['name', 'image', 'category', 'purchase_price']
    success_url = reverse_lazy('catalog:product_list')


    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

