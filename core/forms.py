from django import forms

# Create your views here.


class FindProductForm(forms.Form):
    product_id = forms.IntegerField(label='Input product id', min_value=100, max_value=1000)

class CreateProductForm(forms.Form):
    product_id = forms.IntegerField(label='Input product id', min_value=100, max_value=1000)
    price = forms.IntegerField(label='Input price', min_value=1000)