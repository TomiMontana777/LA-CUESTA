from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'input-group-field',
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'ocupation': forms.Select(
                attrs={
                    'placeholder': 'Ocupacion ...',
                    'class': 'input-group-field',
                }
            ),
            'date_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'Contraseña'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Autenticar usando email como username
        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError('Los datos de usuario no son correctos')

        # Guarda el usuario autenticado
        self.user = user
        return cleaned_data

    def get_user(self):
        return self.user

class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
            'is_active',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres ...',
                    'class': 'input-group-field',
                }
            ),
            'ocupation': forms.Select(
                attrs={
                    'placeholder': 'Ocupacion ...',
                    'class': 'input-group-field',
                }
            ),
            'date_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                },
            ),
        }


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )