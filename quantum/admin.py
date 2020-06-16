from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Contact, Pdf, Register

admin.site.register(Contact)
admin.site.register(Pdf)
admin.site.register(Register)
