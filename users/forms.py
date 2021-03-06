from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = get_user_model()
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(label="Change Profile Picture")
	class Meta:
		model = Profile
		fields = ['image']
