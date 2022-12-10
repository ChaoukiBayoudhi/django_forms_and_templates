from django import forms

from player_app.models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",'placeholder': 'Enter the name of the player','maxlength': 10}),
            'birthDate': forms.DateInput(attrs={'type': 'date','class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"}),
            'country': forms.TextInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",'placeholder': 'Enter the country of the player'}),
            'email': forms.EmailInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",'placeholder': 'Enter the email of the player'}),
            'tshirtNumber': forms.NumberInput(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",'placeholder': 'Enter the tshirt number of the player'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class':"shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"}),
            'gender':forms.Select(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"}),
            'description': forms.Textarea(attrs={'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",'placeholder': 'Enter the description of the player'}),
        }
        labels = {
            'name': 'Player Name',
            'birthDate': 'Player BirthDate',
            'country': 'Player Country',
            'email': 'Player Email',
            'photo': 'Player Photo',
            'gender': 'Player Gender',
            'description': 'Player Description',
        }
        # help_texts = {
        #     'name': 'Enter the name of the player',
        #     'birthDate': 'Enter the birthdate of the player',
        #     'country': 'Enter the country of the player',
        #     'email': 'Enter the email of the player',
        #     'photo': 'Enter the photo of the player',
        # }
        error_messages = {
            'name': {
                'max_length': 'The player name must be less than 100 characters',
                'min_length': 'The player name must be greater than 1 character',
                'invalid': 'The player name is invalid',
                'required': 'The player name is required',

                'no_spaces': 'The player name must not contain any spaces',
                'no_numbers': 'The player name must not contain any numbers',
                'no_special_characters': 'The player name must not contain any special characters',
            },
            'birthDate': {
                'invalid': 'The birthdate is invalid',
                'required': 'The birthdate is required',
            },

        }

        