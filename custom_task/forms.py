from django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=15)
    
    def clean_email(self) -> str:
        """cleaning email with it`s ending"""
        email = self.cleaned_data('email')
        if email and email.endswith('@gmail.com'):
            raise ValidationError('The gmail registration is not avaliable at the moment')
        return email
    
    def clean_phone_number(self) -> str:
        phone = self.cleaned_data.get('phone_number')
        
        if phone and not phone.startswith('+380'):
            raise ValidationError('The Ukrainian phone number starts with "+380", please, enter it correctly')
        
        if phone and not phone[1:].isdigit():
            raise ValidationError('The phone number must only contain digits')
        return phone   
    
    