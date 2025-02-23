from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogTemplateView, CatalogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', CatalogDetailView.as_view(), name='one_product'),
]
