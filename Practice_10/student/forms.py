from django import forms
from student.models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

JOB_CITY_CHOICES = [
    ('Islamabad', 'Islamabad'),
    ('Lahore', 'Lahore'),
    ('Karachi', 'Karachi'),
    ('Peshawar', 'Peshawar'),
    ('Swabi', 'Swabi'),
    ('Mardan', 'Mardan'),
    ('Abbottabad', 'Abbottabad'),
    ('Chakwal', 'Chakwal'),
    ('Rawalpindi', 'Rawalpindi'),
]

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect()
    )
    
    job_city = forms.MultipleChoiceField(
        choices=JOB_CITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Preferred Job Cities",
        help_text="Select one or more cities where you prefer to work"
    )
    class Meta:
        model = Profile
        fields = [
            'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state',
            'mobile', 'email', 'job_city', 'profile_img', 'mv_file'
        ]

        labels = {
            'name': 'Full Name',
            'mobile': 'Mobile Number',
            'dob': 'Date of Birth',
            'pin': 'Pin Code',
            'mv_file': 'Upload Resume',
        }
        
        help_texts = {
            'profile_img': 'Optional: Upload a profile image (JPEG, PNG).',
            'mv_file': 'Optional: Upload your resume (PDF, DOCX).',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'type': 'date'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your area name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '6-digit PIN code'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10-digit mobile number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'job_city': forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}, choices=JOB_CITY_CHOICES),
        }
            