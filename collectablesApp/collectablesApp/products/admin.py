from django.contrib import admin
from .models import ProductTemplate, ProductProduct, ProductImage

# Register your models here.


class ProdTempAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'barcode', 'manufacturer', 'year', 'style', 'author', 'status', 'created_on')
    list_filter = ("status", "manufacturer", "style")
    search_fields = ['parent_name', 'barcode', 'manufacturer', 'content']
    prepopulated_fields = {'slug': ('parent_name',)}


class ProdProdAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'barcode', 'color', 'link', 'template_id', 'author', 'status', 'created_on')
    list_filter = ("status", "short_code", "color")
    search_fields = ['short_code', 'barcode', 'template_id', 'remarks']
    prepopulated_fields = {'slug': ('short_code',)}


class ProdImgAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'author', 'status', 'created_on')
    list_filter = ("status", "product_id", "author")
    search_fields = ['product_id', 'author', 'remarks']
    # prepopulated_fields = {'slug': ('product_id',)}


admin.site.register(ProductTemplate, ProdTempAdmin)
admin.site.register(ProductProduct, ProdProdAdmin)
admin.site.register(ProductImage, ProdImgAdmin)