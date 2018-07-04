from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
#     location = forms.CharField(help_text='Required.')
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','birth_date','location' )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField(help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 
        'last_name', 'email', 'password1', 'password2','birth_date','location' )


class RecordForm(forms.ModelForm):
    bank_name=forms.CharField(label="bank name")
    branch=forms.CharField(label="branch")
    account_name=forms.CharField(label="accont name")
    account_number=forms.IntegerField(label="account number")
    depositors_name=forms.CharField(label="depositors name")
    amount=forms.IntegerField(label="amount")
    comment=forms.CharField(widget=forms.Textarea,label='comment')

    class Meta:
        model = Record
        fields = ('bank_name', 'branch', 
        'account_name', 'account_number', 'depositors_name', 'amount','comment')

