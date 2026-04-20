from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ProductCreateForm
from .models import Product


class ContactsView(ListView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object




class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalog:product_list')


    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

