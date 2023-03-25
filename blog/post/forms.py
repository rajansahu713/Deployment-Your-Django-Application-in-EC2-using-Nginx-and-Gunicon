# from django.core import validators
# from django import forms
# from .models import User



# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm



# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model =User
#         fields =['name', 'email', 'password']

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
#         }



# class Signup(UserCreationForm):
#     password2 =forms.CharField(label="confirm Password(again)",widget=forms.PasswordInput)
#     class Meta:
#         model =User
#         fields = ['username','first_name','last_name','email']
#         labels ={'email':'Email'}