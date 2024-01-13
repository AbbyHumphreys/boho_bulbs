from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, LampType, Colour, Brand, IpRating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        colours = Colour.objects.all()
        lamptypes = LampType.objects.all()
        ipratings = IpRating.objects.all()
        brands = Brand.objects.all()
        colours_friendly_names = [(
                c.id, c.get_friendly_name()) for c in colours]
        lamptypes_friendly_names = [(
                l.id, l.get_friendly_name()) for l in lamptypes]
        ipratings_friendly_names = [(
                i.id, i.get_friendly_name()) for i in ipratings]
        brands_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['colour'].choices = colours_friendly_names
        self.fields['lamptype'].choices = lamptypes_friendly_names
        self.fields['iprating'].choices = ipratings_friendly_names
        self.fields['brand'].choices = brands_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
