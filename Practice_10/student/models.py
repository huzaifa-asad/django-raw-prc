from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError("Pin code must be exactly 6-digits long.")

def mobile_number_len(value):
    if len(str(value)) != 10:
        raise ValidationError("Mobile number must be exactly 10-digit")


STATE_CHOICE = (("AL","Alabama"),("AK","Alaska"),("AZ","Arizona"),("AR","Arkansas"),("CA", "California"),("CO", "Colorado"),
("CT","Connecticut"),("DC","Washington DC"),("DE","Delaware"),("FL","Florida"),("GA","Georgia"),
("HI","Hawaii"),("ID","Idaho"),("IL","Illinois"),("IN","Indiana"),("IA","Iowa"),("KS","Kansas"),("KY","Kentucky"),
("LA","Louisiana"),("ME","Maine"),("MD","Maryland"),("MA","Massachusetts"),("MI","Michigan"),("MN","Minnesota"),
("MS","Mississippi"),("MO","Missouri"),("MT","Montana"),("NE","Nebraska"),("NV","Nevada"),("NH","New Hampshire"),
("NJ","New Jersey"),("NM","New Mexico"),("NY","New York"),("NC","North Carolina"),("ND","North Dakota"),("OH","Ohio"),
("OK","Oklahoma"),("OR","Oregon"),("PA","Pennsylvania"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),
("TN","Tennessee"),("TX","Texas"),("UT","Utah"),("VT","Vermont"),("VA","Virginia"),("WA","Washington"),("WV","West Virginia"),
("WI","Wisconsin"),("WY","Wyoming"))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(
        validators=[validate_pin_length],
        help_text="Enter 6-digit Pin Code")
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    mobile = models.CharField(
        max_length=10,
        # validators=[RegexValidator(regex=r'^/d{10}$')],
        validators=[mobile_number_len],
        help_text='Enter a 10-digit mobile number')
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile_img', blank=True)
    mv_file = models.FileField(upload_to='doc', blank=True)
    