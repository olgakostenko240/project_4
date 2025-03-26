from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product
from catalog.forms import CatalogForms, CatalogModeratorForms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from catalog.services import get_catalog_from_cache, ProductService


class CatalogListView(ListView):
    model = Product

    def get_queryset(self):
        return get_catalog_from_cache()


class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products_id = self.object.id
        # products_id = self.kwargs["pk"]
        context["product"] = ProductService.get_product_by_id(products_id)
        return context


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CatalogForms
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = CatalogForms
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return CatalogForms
        if user.has_perm("catalog.can_unpublish_product"):
            return CatalogModeratorForms
        raise PermissionDenied


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:product_list')


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return CatalogForms
        if user.has_perm("catalog.delete_product"):
            return CatalogModeratorForms
        raise PermissionDenied


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
