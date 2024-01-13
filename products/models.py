from django.db import models


class LampType(models.Model):

    class Meta:
        verbose_name_plural = 'Lamp types'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2500, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class IpRating(models.Model):

    class Meta:
        verbose_name_plural = 'IP ratings'

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=2500, null=True, blank=True)
    friendly_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Colour(models.Model):

    class Meta:
        verbose_name_plural = 'Colours'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):

    class Meta:
        verbose_name_plural = 'Brands'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2500, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    lamptitle = models.CharField(max_length=254)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey(
        'Colour', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description1 = models.TextField(max_length=2500, null=True, blank=True)
    lamptype = models.ForeignKey(
        'LampType', null=True, blank=True, on_delete=models.SET_NULL)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    bulbamount = models.IntegerField(null=True, blank=True)
    wattage = models.IntegerField(null=True, blank=True)
    bulbtype = models.CharField(
        max_length=50, null=True, blank=True)
    iprating = models.ForeignKey(
            'IpRating', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.lamptitle
