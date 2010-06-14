from django.contrib import admin

from multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin

from models import Product, ProductVariant


class ProductVariantInline(MultilingualInlineAdmin):
    model = ProductVariant
    extra = 0
    
    
class ProductAdmin(MultilingualModelAdmin):
    inlines = (
        ProductVariantInline, 
    )


admin.site.register(Product, ProductAdmin)
