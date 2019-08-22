from django.contrib.auth.forms import UserCreationForm as UCreationForm
from django.contrib.auth.forms import UserChangeForm as UChangeForm

from .models import User


class UserCreationForm(UCreationForm):

    class Meta(UCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserChangeForm(UChangeForm):

    class Meta:
        model = User
        fields = UChangeForm.Meta.fields
