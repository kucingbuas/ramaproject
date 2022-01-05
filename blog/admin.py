from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class ArtikelAdmin(ImportExportModelAdmin):
    list_display = ('nama','judul','body','date')

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)