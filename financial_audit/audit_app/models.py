from django.db                                  import models

from django.utils                               import timezone
from phonenumber_field.modelfields              import PhoneNumberField
# Create your models here.

class Contact_Person(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    mobile = PhoneNumberField(blank=True)
    telephone = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=40, blank=True)

    def __str__(self):
        return f'{self.name.upper()}'
class Company(models.Model):
    company_name = models.CharField(max_length=120)
    principal_office = models.CharField(max_length=120)
    sec_reg_no = models.CharField(max_length=11)
    form_type = models.CharField(max_length=4)
    department_requiring_the_report = models.CharField(max_length=4)
    secondary_license_type = models.CharField(max_length=4,blank=True, null=True)
    company_email = models.EmailField(max_length=40)
    mobile = PhoneNumberField(blank=True)
    telephone = PhoneNumberField(blank=True)
    no_of_stockholders = models.IntegerField(default=0)
    annual_meeting = models.DateField(default=timezone.now)
    fiscal_year = models.DateField(default=timezone.now)

    contact_person = models.ForeignKey(Contact_Person, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.form_type = str(self.form_type).upper()
        self.department_requiring_the_report = str(self.department_requiring_the_report).upper()

        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return f'{(self.company_name).upper()}'
