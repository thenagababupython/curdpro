from django import forms

class ProductInsertForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter your product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product_id'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter your product name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter your product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_cost'
            }
        )
    )
    product_color = forms.CharField(
        label="Enter your product color",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_color'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter your product class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_class'
            }
        )
    )

class ProductUpdateForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter your product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product_id'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter your product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_cost'
            }
        )
    )

class ProductDeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter your product id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_id'
            }
        )
    )

