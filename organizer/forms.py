from django import forms
from .models import Tag, NewsLink, Startup

from django.core.exceptions import ValidationError


class SlugCleanMixin:
    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug

class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
    # name = forms.CharField(max_length=31)
    # slug = forms.SlugField(max_length=31, help_text='A label for URL config')
    # def save(self):
    #     new_tag = Tag.objects.create(name=self.cleaned_data['name'], slug=self.cleaned_data['slug'])
        # return new_tag
    def clean_name(self):
        return self.cleaned_data['name'].lower()

class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'

class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'

