from django.contrib import admin
from .models import  *
# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_display = ['title','description']
admin.site.register(Trend,MyAdmin)


