from django.contrib import admin
from .models import *

class ProductVariantInlines(admin.TabularInline):
    model = Vareiants
    extra = 2
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update','sub_category')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'create', 'update', 'amount', 'available', 'unit_price', 'discount', 'total_price', ]
    list_filter = ('available',)
    list_editable = ('amount',)
    raw_id_fields = ('category',)
    inlines = [ProductVariantInlines]


class VariantAdmin(admin.ModelAdmin):
    list_display = ['name','id']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','id']




admin.site.register(Catgory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vareiants,VariantAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Color)