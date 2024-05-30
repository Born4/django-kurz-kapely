from django.contrib import admin

from bands import models


@admin.register(models.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
