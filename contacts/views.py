from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from lxml import etree

from contacts.forms import ContactForm
from contacts.models import Contact
import logging

log = logging.getLogger(__name__)


class ContactlistView(ListView):
    model = Contact
    template_name = 'contacts/contacts-list.html'
    context_object_name = 'contacts'


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contacts/contacts-create.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse(
            "contacts:list",
        )


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:list")
    template_name = 'contacts/contacts-delete.html'


class ContactDetailView(DetailView):
    template_name = 'contacts/contacts-detail.html'
    model = Contact
    form_class = ContactForm


class ContactUpdateView(UpdateView):
    template_name = "contacts/contacts-edit.html"
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        return reverse(
            "contacts:detail",
            kwargs={"pk": self.object.pk},
        )


def import_contacts_from_xml(request):
    if request.method == 'POST':
        xml_file = request.FILES['xml_file']
        tree = etree.parse(xml_file)
        root = tree.getroot()

        # Обработка данных из XML файла и сохранение в базу данных
        for contact in root.findall('contact'):
            # Парсинг данных из XML
            name = contact.find('name').text
            email = contact.find('email').text
            phone = contact.find('phone').text

            # Сохранение данных в базу данных
            contact = Contact(name=name, email=email, phone=phone)
            contact.save()

        return HttpResponse('Данные успешно импортированы')
    return render(request, 'import_products.html')


def export_contacts_to_xml(request):
    # Получение данных из базы данных
    contacts = Contact.objects.all()

    # Создание XML файла
    root = etree.Element('contacts')
    for contact in contacts:
        contact_elem = etree.SubElement(root, 'contact')
        name_elem = etree.SubElement(contact_elem, 'name')
        name_elem.text = contact.name
        email_elem = etree.SubElement(contact_elem, 'email')
        email_elem.text = contact.email
        phone_elem = etree.SubElement(contact_elem, 'phone')
        phone_elem.text = contact.phone

    xml_data = etree.tostring(root, pretty_print=True)

    response = HttpResponse(xml_data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="contacts.xml"'
    return response


