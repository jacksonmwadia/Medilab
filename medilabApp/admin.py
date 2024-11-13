from django.contrib import admin

from medilabApp.models import Patient, Appointment, Contact
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_display_links = ('name',)  # Fields that link to the detail view
    list_per_page = 20  # Controls pagination in admin list view
    ordering = ('name',)  # Sorts the items by name

    class Media:
        css = {
            'all': (static('custom_admin.css'),)  # Path to your custom CSS file
        }

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Contact, ContactAdmin)

