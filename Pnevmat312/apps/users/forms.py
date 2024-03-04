from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):  # Форма регистрации
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(forms.Form):  # Форма авторизации
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class ChangeUserProfileForm(forms.Form):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Логин'}), required=False)
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'placeholder': 'Почта'}), required=False)
    password = forms.CharField(label='Старый пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_new = forms.CharField(label='Новый пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}))
    password_again = forms.CharField(label='Повторите пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите новый пароль'}))



class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })