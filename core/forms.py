from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Introduce tu email.',
            'class': 'input-obj',
            }),
        )
    password = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Introduce tu contraseña.',
            'class': 'input-obj',
            }),
        )