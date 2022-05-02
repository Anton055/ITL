from django.contrib import admin
from .models import EmpModel

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'salary',)
admin.site.register(EmpModel, EmpAdmin)