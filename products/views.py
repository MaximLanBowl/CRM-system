from decimal import Decimal

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from lxml import etree

from .models import Product
from .forms import ProductForm
import logging

from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime, timedelta


log = logging.getLogger(__name__)


class ProductsListView(ListView):
    template_name = 'products/products-list.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'products'


class ProductsCreateView(CreateView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:list')
    form_class = ProductForm


class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products:list")
    template_name = 'products/products-delete.html'


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    template_name = "products/products-edit.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse(
            "products:details",
            kwargs={"pk": self.object.pk},
        )


def import_products_from_xml(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    for product_xml in root.iter('product'):
        name = product_xml.find('name').text
        description = product_xml.find('description').text
        price = Decimal(product_xml.find('price').text)
        quantity = int(product_xml.find('quantity').text)

        Product.objects.create(name=name, description=description, price=price, quantity=quantity)


def export_products_to_xml(request):
    products = Product.objects.all()
    xml_generated = False

    root = etree.Element('products')
    for product in products:
        product_xml = etree.Element('product')
        etree.SubElement(product_xml, 'name').text = product.name
        etree.SubElement(product_xml, 'description').text = product.description
        etree.SubElement(product_xml, 'price').text = str(product.price)
        etree.SubElement(product_xml, 'quantity').text = str(product.quantity)

        root.append(product_xml)
        xml_generated = True

    tree = etree.ElementTree(root)
    tree.write('products.xml', xml_declaration=True, encoding='utf-8', pretty_print=True)
    return render(request, 'products/export_products.html', {'xml_generated': xml_generated})


def products_report(request):
    products = Product.objects.all()
    return render(request, 'products/products_report.html', {'products': products})
