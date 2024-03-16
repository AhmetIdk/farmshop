from django.contrib import admin

from home.models import *

# Register your models here.
admin.site.register(Setting)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['subject','name', 'email']
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)