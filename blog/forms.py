from django import forms
from .models import Blog

class BlogFormCreate(forms.ModelForm):

    class Meta:
        model  = Blog
        fields = ['title', 'content', 'image', 'publication_status']


    def __init__(self, *args, **kwargs):
        super(BlogFormCreate, self).__init__(*args, **kwargs)


        for field_name in self.fields:
            self.fields[field_name].help_text = ''


        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите название',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите контент',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите изображение',
        })
        self.fields['publication_status'].widget.attrs.update({
            'class': 'form-check-input',
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







