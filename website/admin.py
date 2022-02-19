from ast import Delete
from dataclasses import field, fields
from django.contrib import admin
from website import models
from django.utils.html import format_html
#customization
class DoctorAdmin(admin.ModelAdmin):
    list_display=('Name','Field')
    list_filter=('Field',)
class FieldAdmin(admin.ModelAdmin):
    field=('Field','About')
    list_display=('Field','About')
class SliderAdmin(admin.ModelAdmin):
    list_display=('Header','Data')
class QueryAdmin(admin.ModelAdmin):
    list_display=('Name','Sub')    
# Register your models here.
admin.site.register(models.Doctor,DoctorAdmin)
admin.site.register(models.field,FieldAdmin)
admin.site.register(models.Slider,SliderAdmin)
admin.site.register(models.Query,QueryAdmin)
admin.site.register(models.department)
admin.site.register(models.Facilities_no)