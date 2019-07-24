from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('nama_file','tanggalinput', 'jaminput','integ','isi','tempat')
