from django.contrib import admin
from .models import Flan, ContactForm

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_private', 'slug')
    list_filter = ('is_private',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_name', 'customer_email', 'message')
