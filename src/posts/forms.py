from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content'
        ]

    def clean_content(self,*args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "":
            raise forms.ValidationError("Field cannot be empty")
        return content

