from django.contrib import admin
from deply.models import Fabu
import logging
import django.utils.log
import logging.handlers

# Register your models here.
@admin.register(Fabu)
class DeplyAdmin(admin.ModelAdmin):
    #fileds控制增加页面元素，list_display控制显示页面元素
    fields = ('version', 'servername', 'linenos')
    exclude = ['product' ]
    list_display = [
            'version',
            'servername',
            'product',
            'linenos',
            'created',
                   ]
    list_per_page= 100
    list_filter = ['product', 'servername', 'created']
    search_fields = ['version', 'servername' ]
    actions_on_top = False
    actions_on_bottom = True
    #date_hierarchy = 'created'

    #根据用户判断显示内容
    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """
        if request.user == 'hjw':
            self.list_display = ('version', 'servername', 'product','created')
        else:
            self.list_display = ('version', 'created')
        return self.list_display
