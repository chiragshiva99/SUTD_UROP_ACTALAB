from typing import Text
from django import forms
from .models import Customer, DetailsOfDataCollection, MaterialList, TxtFile
from .views import *

class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = Customer 
        fields = ("username", "password","full_name", "email")

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():   
            raise forms.ValidationError("Username already exists. Please choose another username.")
        return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class DataCollectionForm(forms.ModelForm):
    
    class Meta:
        model = DetailsOfDataCollection
        fields = ("instru_datatype", "operator", "sample_id", "composition", "upload_data", "comments")


class TxtFileForm(forms.ModelForm):

    class Meta:
        model = TxtFile
        fields = ("name", "material_name", "txtfile")



class MaterialListForm(forms.ModelForm):
    class Meta:
        model = MaterialList
        fields = ("material", "source_of_data", "date_added")

