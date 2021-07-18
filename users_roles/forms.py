from django.forms import ModelForm, ModelChoiceField, CharField
from .models import Profile, Groups
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserForm(ModelForm):
    password = CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'is_admin', 'group', 'password']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['group_name', 'group_description']


class LogInForm(AuthenticationForm):
    username = ModelChoiceField(queryset=Profile.objects.all(), to_field_name="username")

    class Meta:
        model = Profile
        fields = ['username', 'password']


