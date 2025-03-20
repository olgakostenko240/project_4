from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class CatalogForms(StyleFormMixin, ModelForm):
    words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "owner")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in self.words:
            if word in name.lower():
                raise ValidationError(f'В названии продукта неможет быть слова {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in self.words:
            if word in description.lower():
                raise ValidationError(f'В описании продукта неможет быть слова {word}')
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной.')
        return price


class CatalogModeratorForms(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        fields = ("status_publication",)