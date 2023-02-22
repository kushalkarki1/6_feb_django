from django import forms
from post.models import Post


# class PostForm(forms.Form):
#     description = forms.CharField(widget=forms.Textarea)
#     image = forms.ImageField(widget=forms.ClearableFileInput, required=False)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("description", "image", "status", )
        # exclude = ("user", )