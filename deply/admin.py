from django.contrib import admin
from deply.models import Fabu

# Register your models here.
class DeplyAdmin(admin.ModelAdmin):
    list_display = [
            'version',
            'servername',
            'product',
            #'ip',
                   ]
    list_per_page= 100
    list_filter = ['product', 'servername']
    search_fields = ['version', 'servername' ]
admin.site.register(Fabu, DeplyAdmin)