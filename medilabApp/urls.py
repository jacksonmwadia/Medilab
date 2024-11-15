
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('view-appointments/', views.view_appointment, name='view-appointments'),
    path('view-contacts/', views.view_contact, name='view-contacts'),
    path('delete/<int:appoint_id>', views.delete_appointment, name='delete_appointment'),
    # path('delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('edit-appointment/<int:appoint_id>/', views.edit_appointment, name='edit_appointment'),


]
