from django import forms

from .models import Goods


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'unit_price', 'price', 'supplier')

    def __init__(self, *args, **kwargs):
        super(GoodsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
