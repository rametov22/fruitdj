from django import forms
from .models import *


class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopModel
        fields = '__all__'


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=20)
    mobile = forms.CharField(max_length=20)
    email = forms.EmailField()
    shipping_method = forms.ChoiceField(choices=[], widget=forms.RadioSelect)
    payment_method = forms.ModelChoiceField(queryset=PaymentMethod.objects.all())
    order_notes = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['shipping_method'].choices = [(method.id, f"{method.name} - ${method.price}") for method in
                                                  ShippingMethod.objects.all()]