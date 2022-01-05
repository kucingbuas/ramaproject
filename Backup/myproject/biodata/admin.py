from django.contrib import admin

# Register your models here.
from . models import Biodata

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user', 'nama','telp','alamat')

admin.site.register(Biodata, BiodataAdmin)