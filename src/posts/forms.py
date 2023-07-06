from django import forms 
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Deja tu comentario'}),
    )
    
    class Meta:
        model = Comment
        fields = ['content']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = 'Deja tu comentario:'
        self.fields['content'].widget.attrs.update({'class': 'textarea'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Deja tu comentario'})
        self.fields['content'].label_tag = '<label class="label" for="%s">%s</label>'
