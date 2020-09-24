from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserCreateForm(UserCreationForm):

    class Meta():
        fields = ('first_name','last_name','username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'



class UserProfilePic(forms.ModelForm):
    class Meta():
        fields = ('profile_pic',)
        model = User

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['profile_pic'].label = 'Profile Image'
