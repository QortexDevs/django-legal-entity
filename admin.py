from django.contrib import admin

from .models import LegalEntity, CEO, Bank

admin.site.register(Bank)
admin.site.register(LegalEntity)
admin.site.register(CEO)
