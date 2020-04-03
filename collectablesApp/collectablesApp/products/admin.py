from django.contrib import admin
from .models import ProductTemplate

# Register your models here.


class ProdTempAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'barcode', 'manufacturer', 'year', 'style', 'author', 'status', 'created_on')
    list_filter = ("status", "manufacturer", "style")
    search_fields = ['parent_name', 'barcode', 'manufacturer', 'content']
    prepopulated_fields = {'slug': ('parent_name',)}


admin.site.register(ProductTemplate, ProdTempAdmin)