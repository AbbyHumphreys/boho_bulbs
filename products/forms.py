from django import forms
from .models import Product, LampType, Colour, Brand, IpRating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        colours = Colour.objects.all()
        lamptypes = LampType.objects.all()
        ipratings = IpRating.objects.all()
        brands = Brand.objects.all()
        colours_friendly_names = [(c.id, c.get_friendly_name()) for c in colours]
        lamptypes_friendly_names = [(c.id, c.get_friendly_name()) for l in lamptypes]
        ipratings_friendly_names = [(c.id, c.get_friendly_name()) for i in ipratings]
        brands_friendly_names = [(c.id, c.get_friendly_name()) for b in brands]


        self.fields['colours'].choices = friendly_names
        self.fields['lamptypes'].choices = friendly_names
        self.fields['ipratings'].choices = friendly_names
        self.fields['brands'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'