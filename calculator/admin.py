from django.contrib import admin
from .models import *
admin.site.register(Country)
admin.site.register(Company)
admin.site.register(AdditionalInformation)
class MyAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone','weight','country','company_price','company_name','length','width','height','email','message')

admin.site.register(save_data,MyAdmin)
# Register your models here.
admin.site.register(Index)