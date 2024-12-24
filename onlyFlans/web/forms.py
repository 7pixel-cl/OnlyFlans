from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre',
                'required': True
            }),
            'customer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tu mensaje',
                'rows': 4,
                'required': True
            }),
        }
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Correo electrónico',
            'message': 'Mensaje',
        }
        error_messages = {
            'customer_email': {
                'invalid': 'Por favor, ingresa una dirección de correo electrónico válida.',
                'required': 'El correo electrónico es obligatorio.',
            },
            'customer_name': {
                'required': 'El nombre es obligatorio.',
            },
            'message': {
                'required': 'El mensaje es obligatorio.',
            },
        } 