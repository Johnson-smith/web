from django.contrib import admin
from hostinfo.models import Host
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = [
            'product',
            'hostname',
            'publicip',
            'publicip1',
            'privateip',
            #'processor_cores',
            'cpu_num',
            'memory',
            'app_name',
            'account',
                   ]
    list_per_page= 100
    list_filter = ['product', 'account']
    search_fields = ['product', 'privateip', 'app_name', 'account' ]
admin.site.register(Host, HostAdmin)