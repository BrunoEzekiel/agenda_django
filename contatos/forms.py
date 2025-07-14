from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o telefone'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome and len(nome) < 2:
            raise forms.ValidationError('O nome deve ter pelo menos 2 caracteres.')
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and len(telefone) < 8:
            raise forms.ValidationError('O telefone deve ter pelo menos 8 dígitos.')
        return telefone
