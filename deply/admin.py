from django.contrib import admin
from deply.models import Fabu

# Register your models here.
@admin.register(Fabu)
class DeplyAdmin(admin.ModelAdmin):
    list_display = [
            'version',
            'servername',
            'product',
            #'ip',
            'linenos',
            #'language',
            #'style',
            'created',

                   ]
    list_per_page= 100
    list_filter = ['product', 'servername']
    search_fields = ['version', 'servername' ]
