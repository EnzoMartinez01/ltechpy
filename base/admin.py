from django.contrib import admin

from base.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'description', 'telephone', 'atendido')
    list_filter = ('atendido', 'email')