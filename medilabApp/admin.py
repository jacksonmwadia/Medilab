from django.contrib import admin

from medilabApp.models import Patient, Appointment, Contact, User1, ImageModel
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


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'department', 'doctor', 'message' )
    list_display_links = ('name',)  # Fields that link to the detail view
    list_per_page = 20  # Controls pagination in admin list view
    ordering = ('name',)  # Sorts the items by name

    class Media:
        css = {
            'all': (static('custom_admin.css'),)  # Path to your custom CSS file
        }

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'password' )
    list_display_links = ('name',)  # Fields that link to the detail view
    list_per_page = 20  # Controls pagination in admin list view
    ordering = ('name',)  # Sorts the items by name

    class Media:
        css = {
            'all': (static('custom_admin.css'),)  # Path to your custom CSS file
        }

admin.site.register(Patient)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(User1, UserAdmin)
admin.site.register(ImageModel)

