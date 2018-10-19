from django.db import models, migrations, connection
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils.encoding import python_2_unicode_compatible
import datetime

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
@python_2_unicode_compatible
class Fabu(models.Model):
    created = models.DateTimeField('发布时间', auto_now_add=True)
    version = models.CharField('git_version',max_length = 100)
    servername = models.CharField('应用',max_length = 100,  null=True)
    product = models.CharField('环境',max_length = 50,null=True)
    linenos = models.BooleanField(default=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    def __str__(self):
        dt_obj = self.created + datetime.timedelta(hours=+8)
        return dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    class Meta:
        get_latest_by = 'created'
        verbose_name = '标签'
        verbose_name_plural = '发布记录'
        #ordering = ('created',)
        ordering = []
        #设置获取最新记录的默认fields
        get_latest_by = ('created')

