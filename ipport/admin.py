from django.contrib import admin
from ipport.models import Yinshe
# Register your models here.

@admin.register(Yinshe)
class IPPORTAdmin(admin.ModelAdmin):
    list_display = [
            'publicip',
            'publicip_port',
            'parviteip',
            'parviteip_port',
            'Agreement',
            'product',
                   ]
    list_per_page= 100
    list_filter = ['Agreement', 'product']
    search_fields = ['parviteip', 'Agreement' ]