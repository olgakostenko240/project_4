from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Product
from catalog.forms import CatalogForms
from django.contrib.auth.mixins import LoginRequiredMixin


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product


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


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:product_list')


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
