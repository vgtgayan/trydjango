from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name        = forms.CharField(
                                    widget=forms.TextInput(attrs={'placeholder':'Product Title'})
                                    )
    description = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'row':5, 'cols':50, 'placeholder':'Product Description'}))
    price       = forms.DecimalField(decimal_places=2, initial=0.00)
    summary = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'row':20, 'cols':100, 'placeholder':'Product Summary'}))
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'summary',
            'featured'
        ]
    # Input validation (overrides django validation)----------
    # Validate price and return validated data
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price cannot be $0.00')
        return price

# Raw django form
class RawProductForm(forms.Form):
    name        = forms.CharField(
                                    widget=forms.TextInput(
                                        attrs={'placeholder':'Product Title'})
                                 ) 
    description = forms.CharField(required=False,
                                widget=forms.Textarea(
                                    attrs={'row':20, 'cols':100, 'placeholder':'Product Description'}
                                    )
                                )
    price       = forms.DecimalField(decimal_places=2)
    summary     = forms.CharField()
    
