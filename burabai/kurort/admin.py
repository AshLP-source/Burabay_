from django.contrib import admin
from . import models
from .models import Requests
from django.contrib import admin

# admin.site.register(models.Requests,RequestsAdmin)
@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    model = Requests
    list_display = ('id','name', 'phone_number', 'adult' , 'child', 'hotel', 'date1', 'date2')



