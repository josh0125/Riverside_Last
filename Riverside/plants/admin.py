from django.contrib import admin
from django.http import HttpResponse
import csv

# Register your models here.

from .models import Plant, Category, Subcategory, Sun_Exposure, Soil_Type, Soil_Moisture, Habit

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    search_fields = ['variety']
    readonly_fields = ['img_preview']

    change_form_template = 'custom_change_form.html'

admin.site.register(Plant, PlantAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Sun_Exposure)
admin.site.register(Soil_Type)
admin.site.register(Soil_Moisture)
admin.site.register(Habit)
