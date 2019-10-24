from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder":"New product title."
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description field",
                "class": "class_name",
                "rows": 15,
                "cols": 50
            }
        )
    )
    price = forms.DecimalField(initial=1000.00)
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'price',
            'summary',
            'featured'
        ]
    # def clean_title(self,*args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid Title")
    #     else:
    #         return title
            

class RawProductCreateForm(forms.Form):
    title       =   forms.CharField(required=True, widget=forms.TextInput(attrs={
        "placeholder":"New product title."
    }))
    description =   forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Description field",
                                "class": "class_name",
                                "rows": 15,
                                "cols": 50
                            }
                        )
                    )
    price       =   forms.DecimalField(initial=1000.00)