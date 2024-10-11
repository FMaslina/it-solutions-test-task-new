from django import forms

from cars.models import Comment, Car


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Комментарий',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

