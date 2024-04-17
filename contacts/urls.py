from django.urls import path
from . import views
from .views import (
    ContactDeleteView,
    ContactDetailView,
    ContactCreateView,
    ContactlistView,
    ContactUpdateView
)

app_name = 'contacts'

urlpatterns = [
    path('', ContactlistView.as_view(), name='list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='edit'),
    path('new/', ContactCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='delete'),
    path('import-contacts-from-xml/', views.import_contacts_from_xml, name='import_contacts_from_xml'),
    path('export-contacts-to-xml/', views.export_contacts_to_xml, name='export_contacts_to_xml'),

]
