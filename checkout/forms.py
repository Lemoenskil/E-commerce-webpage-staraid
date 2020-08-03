from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = (
            'credit_card_number', 'cvv', 'expiry_month', 'expiry_year', 'stripe_id')
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('credit_card_number', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cvv', css_class='form-group col-md-03 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('expiry_month', css_class='form-group col-md-04 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('expiry_year', css_class='form-group col-md-04 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('stripe_id', css_class='form-group col-md-04 mb-0'),
                css_class='form-row'
            ),
        )
    


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode','town_or_city', 'street_address1', 'street_address2' )
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('full_name', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                Column('country', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('town_or_city', css_class='form-group col-md-6 mb-0'),
                Column('postcode', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('street_address1', css_class='form-group col-md-6 mb-0'),
                Column('street_address2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )

