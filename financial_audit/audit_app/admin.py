from django.contrib import admin
from decimal import Decimal
# MODELS

from audit_app.models import *

class PostCompanyProfile(admin.ModelAdmin):
    list_display = ('company_name','contact_person')


admin.site.register(Company, PostCompanyProfile)
admin.site.register(Contact_Person)
# Register your models here.
