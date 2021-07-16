from django.forms import ModelForm
from .models import Profile, Groups


class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username_p', 'is_admin', 'group']


class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['group_name', 'group_description']