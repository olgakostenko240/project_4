from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
