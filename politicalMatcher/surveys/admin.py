from django.contrib import admin

# Register your models here.
from . import models

class SurveysAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Surveys, SurveysAdmin)