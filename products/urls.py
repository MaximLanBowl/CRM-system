from django.urls import path
from . import views
from .views import (
    ProductsListView,
    ProductsCreateView,
    ProductsDeleteView,
    ProductsDetailView,
    ProductUpdateView,
)

app_name = 'products'

urlpatterns = [
    path('new/', ProductsCreateView.as_view(), name='create'),
    path('', ProductsListView.as_view(), name='list'),
    path('<int:pk>/delete/', ProductsDeleteView.as_view(), name='delete'),
    path('<int:pk>', ProductsDetailView.as_view(), name='details'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='update'),
    path('import-products-from-xml/', views.import_products_from_xml, name='import_products_from_xml'),
    path('export-products-to-xml/', views.export_products_to_xml, name='export_products_to_xml'),
    path('products_report/', views.products_report, name='products_report'),

]
