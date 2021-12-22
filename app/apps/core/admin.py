from django.contrib import admin

from .models import Workstation, Owner, Report

admin.site.register(Workstation)
admin.site.register(Owner)
admin.site.register(Report)
