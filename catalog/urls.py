from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogTemplateView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='product_list'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', CatalogDetailView.as_view(), name='product_detail'),
    path('products/create/', CatalogCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', CatalogUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', CatalogDeleteView.as_view(), name='product_delete')
]
