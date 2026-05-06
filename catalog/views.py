from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ProductCreateForm, ProductModeratorForm
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




class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalog:product_list')


    def get_form_class(self):
        user = self.request.user
        self.object = self.get_object()
        if user == self.object.owner:
            return ProductCreateForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user == self.object.owner or request.user.has_perm("catalog.delete_product"):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

