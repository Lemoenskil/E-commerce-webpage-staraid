from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Enter Message"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('content', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('contact_name', css_class='form-group col-md-6 mb-0'),
                Column('contact_email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

        )