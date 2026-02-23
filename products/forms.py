from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")

        if not "abc" in title:
            raise forms.ValidationError("No abc in title")
        
        return title

class RawProductForm(forms.Form):
    title       = forms.CharField(label='Label dede ladle', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(
                            required=False, 
                            widget=forms.Textarea({
                                "class": "my-class",
                                "rows": 20
                            })
                        )
    price       = forms.DecimalField(initial=122)