from django.contrib import admin
from farmshop.settings import DEFAULTS
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from product.models import *

from django.utils.safestring import mark_safe

# Register your models here.

# categories
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count', 'image_tag')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category_id',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category_id',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
admin.site.register(Category, CategoryAdmin2)

#product image fields
class ProductImagesInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_tag']

#products
class ProductAdmin(admin.ModelAdmin):
    # fields=['title','status']
    list_display = ['title', 'status', 'image_tag']
    # list_display = ['title', 'status']
    list_filter = ['status', 'category_id']
    # readonly_fields = ('image_tag',)
    inlines=[ProductImagesInline]
    prepopulated_fields = {"slug": ("title",)}  # new
admin.site.register(Product, ProductAdmin)

#product images
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_name', 'image_tag']
admin.site.register(Image, ImageAdmin)

#gallery images
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
admin.site.register(GalleryImage, GalleryImageAdmin)

#comments
class CommentAdmin(admin.ModelAdmin):
    list_display=['subject', 'product', 'rate']
admin.site.register(Comment, CommentAdmin)
