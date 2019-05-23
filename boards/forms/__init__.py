from django import forms

class NewPostForm(forms.Form):
    post_title = forms.CharField(label='Post Title', max_length=20)
    post_content = forms.CharField(widget=forms.Textarea)