from django.contrib import admin

# Register your models here.
from obfuscate.models import link

class linkadmin(admin.ModelAdmin):
    list_display = ('obf_id','target','clicks')

admin.site.register(link, linkadmin)
