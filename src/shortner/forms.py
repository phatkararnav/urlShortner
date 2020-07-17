from django import forms

from .validators import validate_url


class submitUrlForm(forms.Form):
    url = forms.CharField(label = '', validators=[validate_url], widget = forms.TextInput(attrs={"placeholder": "Insert URL", "class": "form-control"}))


  



#url = forms.CharField(label = 'Submit URL', validators=[validate_url])