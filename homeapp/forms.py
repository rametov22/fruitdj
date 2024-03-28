from django import forms
from .models import *
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = HomeModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Имя',
                    'class': 'form-control',
                    'type': 'text'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Почта',
                    'class': 'form-control',
                    'type': 'email'
                }
            ),
            'person': forms.NumberInput(
                attrs={
                    'placeholder': 'Персона',
                    'class': 'form-control',
                    'type': 'text'
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'placeholder': 'Номер',
                    'class': 'form-control',
                    'type': 'text'
                }
            ),
            'date': forms.DateInput(format=settings.DATE_INPUT_FORMATS,
                                    attrs={
                                        'placeholder': 'Дата',
                                        'class': 'form-control gj-textbox-md',
                                        'id': "datepicker"
                                    }
                                    ),
            'time': forms.Select(
                attrs={
                    'placeholder': 'Время',
                    'class': 'form-control',
                }
            ),
            'note': forms.Textarea(
                attrs={
                    'placeholder': 'Заметки',
                    'class': 'form-control',
                }
            )
        }

    def clean_name(self):
        data = self.cleaned_data["name"]
        return data


class RegForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'name': 'username',
        'placeholder': 'Логин',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Логин'",
        'class': "single-input",
    }))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'name': 'username',
        'placeholder': 'Имя',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Имя'",
        'class': "single-input",
    }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'name': 'username',
        'placeholder': 'Фамилия',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Фамилия'",
        'class': "single-input",
    }))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={
        'name': 'email',
        'placeholder': 'Почта',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Почта'",
        'class': "single-input",
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'name': 'password1',
        'placeholder': 'Пароль',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Пароль'",
        'class': "single-input",
    }))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={
        'name': 'password2',
        'placeholder': 'Повтор пароля',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Повтор пароля'",
        'class': "single-input",
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'name': 'username',
        'placeholder': 'Логин',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Логин'",
        'class': "single-input",
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'name': 'password',
        'placeholder': 'Пароль',
        'onfocus': "this.placeholder = ''",
        'onblur': "this.placeholder = 'Пароль'",
        'class': "single-input",
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class CommentForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = BlogComments
        fields = ('comment', 'stars',)
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 30, 'rows': 9, 'class': 'form-control w-100', 'placeholder': 'Your Review *', 'spellcheck': 'false'}),
        }


class ReviewForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = ReviewModel
        fields = ['name', 'email', 'text', 'stars']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-100 form-control border-0 py-3 mb-4', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'w-100 form-control border-0 py-3 mb-4', 'placeholder': 'Enter Your Email'}),
            'text': forms.Textarea(attrs={'class': 'w-100 form-control border-0 mb-4', 'rows': 5, 'cols': 10,
                                          'placeholder': 'Your Message'}),
        }
        labels = {
            'name': '',
            'email': '',
            'text': '',
        }
