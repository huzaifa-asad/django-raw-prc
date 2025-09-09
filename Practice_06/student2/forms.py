from django import forms
from django.core.validators import MinLengthValidator


# Field Type Examples
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

class DemoForm(forms.Form):
    # Basic Fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()

    # Additional Fields Types
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointment_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()
    
    # Choices Fields
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    interests = forms.MultipleChoiceField(choices=[
        ('tech', 'Technology'), ('art', 'Art'), ('sports', 'Sports')
    ])