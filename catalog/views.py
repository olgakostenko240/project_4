from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product
from catalog.forms import CatalogForms


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    form_class = CatalogForms
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog/product_list')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = CatalogForms
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog/product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class CatalogDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:product_list')


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
