
from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()  # Ensure this field is either naive or aware, depending on your setting.
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
      # Optional if it's a ForeignKey
    message = models.TextField()

    def __str__(self):
        return self.name

def validate_no_empty(value):
    if not value or value.isspace():
        raise ValidationError('This field cannot be empty or contain only spaces.')

class Contact(models.Model):
    name = models.CharField(max_length=100, validators=[validate_no_empty])
    email = models.EmailField(validators=[validate_no_empty])
    subject = models.CharField(max_length=200, validators=[validate_no_empty])
    message = models.TextField(validators=[validate_no_empty])

    def __str__(self):
        return self.name + "\t" + self.email  # Tab space between name and email

class User1(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    username = models.CharField(max_length=150, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name
