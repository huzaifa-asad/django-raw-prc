from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    # to Validate specific field in Form
    def clean_name(self):
        # name_value = self.cleaned_data.get('name')
        name_value = self.cleaned_data['name']
        if len(name_value) < 4:
            raise forms.ValidationError('name', 'Enter more than or equal 4 characters')
        return name_value
    
    
    # For Multiple Validated Fields
    def clean(self):
        cleaned_data = super().clean()
        email_value = cleaned_data.get('email')
        password_value = cleaned_data.get('password')
        special_chars = "!@#$%^&*({}[]?><,/"
        
        if email_value and len(email_value) < 10:
            self.add.error('email', 'Enter a valid email')
        
        if password_value:
            if len(password_value) < 8 or not any(char in special_chars for char in password_value):
                self.add_error('password', 'Enter correct password: minimum 8 characters including a special character')
        
        return cleaned_data
    