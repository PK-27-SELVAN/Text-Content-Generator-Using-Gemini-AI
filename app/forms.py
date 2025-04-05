from django import forms

class ContentForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your content request..',
            'class': 'search-input',
            'autofocus': True
        }),
        label='',
        help_text='Be specific - include content type, topic, keywords, and preferred tone'
    )