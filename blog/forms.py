from typing import Text
from django import forms
from .models import Customer, DetailsOfDataCollection, MaterialList, TxtFile
from .views import *


class CustomerRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Full Name",
            "class": "form-control"
        }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Username",
            "class": "form-control"
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password",
            "class": "form-control"
        }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Re-Enter Password",
            "class": "form-control"
        }))

    class Meta:
        model = Customer
        fields = (
            "full_name",
            "email",
            "username",
            "password",
            "confirm_password",
        )

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Username already exists. Please choose another username.")
        return uname

    def clean(self):
        cleaned_data = super(CustomerRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
        if (len(password) < 9):
            self.add_error('password',
                           'Use a password with a minimum of 10 charcters.')
        if password.isdigit():
            self.add_error(
                'password',
                'password must contains both aplhabets and numbers')
        return cleaned_data


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class DataCollectionForm(forms.ModelForm):
    class Meta:
        model = DetailsOfDataCollection
        fields = ("instru_datatype", "operator", "sample_id", "composition",
                  "upload_data", "comments")


class TxtFileForm(forms.ModelForm):
    class Meta:
        model = TxtFile
        fields = ("name", "material_name", "txtfile")


class MaterialListForm(forms.ModelForm):
    class Meta:
        model = MaterialList
        fields = ("material", "source_of_data", "date_added")
