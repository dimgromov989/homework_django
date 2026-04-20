from django import forms
from .models import Blog


class StyleFormMixin:
    """Bootstrap-классы для полей формы и отключение help_text по умолчанию."""

    input_css_class = "form-control"
    checkbox_css_class = "form-check-input"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ""
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                css = self.checkbox_css_class
            else:
                css = self.input_css_class
            classes = widget.attrs.get("class", "")
            widget.attrs["class"] = (f"{classes} {css}").strip() if classes else css


class BlogFormCreate(StyleFormMixin, forms.ModelForm):

    class Meta:
        model  = Blog
        fields = ['title', 'content', 'image', 'publication_status']


    def __init__(self, *args, **kwargs):
        super(BlogFormCreate, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Выберите название',
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Выберите контент',
        })
        self.fields['image'].widget.attrs.update({
            'placeholder': 'Выберите изображение',
        })



    def clean_title(self):
        title = self.cleaned_data.get('title')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in title.lower():
                raise forms.ValidationError("Название не может содержать запрещенные слова")
        return title


    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("Контент должен быть длиннее 10 символов")
        return content







