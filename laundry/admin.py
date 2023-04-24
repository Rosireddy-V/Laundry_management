from django.contrib import admin
from .models import *

# Register your models here.
class clothesAdmin(admin.ModelAdmin):
    list_display=('std','id','std_id','get_total','Date','status')
    search_fields=['id']
admin.site.register(clothes,clothesAdmin)

class queryAdmin(admin.ModelAdmin):
    list_display=('Laundry_id','Problem','Date')
    search_fields=['Laundry_id']

admin.site.register(query,queryAdmin)
