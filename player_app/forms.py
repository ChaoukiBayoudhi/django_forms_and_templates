from django import forms

from player_app.models import Player


class PlayerForm(forms.ModelForm):
    
    class Meta:
        model = Player
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthDate': forms.DateInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tshirtNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Player Name',
            'birthDate': 'Player BirthDate',
            'country': 'Player Country',
            'email': 'Player Email',
            'photo': 'Player Photo',
        }
        help_texts = {
            'name': 'Enter the name of the player',
            'birthDate': 'Enter the birthdate of the player',
            'country': 'Enter the country of the player',
            'email': 'Enter the email of the player',
            'photo': 'Enter the photo of the player',
        }
        error_messages = {
            'name': {
                'max_length': 'The player name must be less than 100 characters',
            },

        }

        