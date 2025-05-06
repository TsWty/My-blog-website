from django import forms
from django.utils.text import slugify
from .models import Post
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
            'tags': forms.CheckboxSelectMultiple,
        }
    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data['title'])
        return slug
    