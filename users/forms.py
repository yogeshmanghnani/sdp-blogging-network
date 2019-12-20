from pprint import pprint 
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

class MyImageField(forms.widgets.ClearableFileInput):
	template_name = "users/widgets/profile_button.html"

class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(widget=MyImageField())
	class Meta:
		model = Profile
		fields = ['image']
