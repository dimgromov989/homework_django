from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'purchase_price', 'publication_status']

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)


        for field_name in self.fields:
            self.fields[field_name].help_text = ''

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите название',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите изображение',
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-select',
        })
        self.fields['purchase_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену',
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError("Название не может содержать запрещенные слова")
        return name
        

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ")
        return image

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price <= 0:
            raise forms.ValidationError("Цена не может быть отрицательной или равна нулю")
        return purchase_price



class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['publication_status']

    def clean_publication_status(self):
        publication_status = self.cleaned_data.get("publication_status")
        # Модератор может только отменять публикацию, а не публиковать.
        if publication_status is True:
            raise forms.ValidationError("У вас нет прав публиковать продукт.")
        return publication_status
