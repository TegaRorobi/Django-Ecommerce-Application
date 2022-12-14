from .models import *
from django import forms


# class SellerForm(forms.ModelForm):
#     class Meta:
#         model = Seller
#         fields = ['name', 'location', 'contact', 'about', 'image']
# class PhoneForm(forms.ModelForm):
#     class Meta:
#         model = Phone
#         fields = '__all__'

# class UserImageForm(forms.ModelForm):
#     class Meta:
#         model = PhoneImage
#         fields ='__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email']

    def clean_first_name(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) <3:
            raise forms.ValidationError('Please enter a valid first name')
        return first_name
    def clean_last_name(self, *args, **kwargs):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) <3:
            raise forms.ValidationError('Please enter a valid last name')
        return last_name
         