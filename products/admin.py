from django.contrib import admin
from .models import Product, Brand, Colour, IpRating, LampType


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "lamptitle",
        "brand",
        "colour",
        "sku",
        "price",
        "lamptype",
        "bulbtype",
        "iprating",
        "image",
    )

    ordering = ('sku',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


class LampTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


class IpRatingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )


class ColourAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
    )



admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(IpRating, IpRatingAdmin)
admin.site.register(LampType,LampTypeAdmin)
