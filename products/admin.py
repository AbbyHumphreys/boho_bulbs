from django.contrib import admin
from .models import Product, Brand, Colour, IpRating, LampType

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(IpRating)
admin.site.register(LampType)
