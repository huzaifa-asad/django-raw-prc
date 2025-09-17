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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
            