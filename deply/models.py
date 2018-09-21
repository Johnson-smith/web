from django.db import models, migrations, connection, models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Fabu(models.Model):
    PRODUCT_CHOICES = (
            (u'prod', u'prod'),
            (u'test', u'test'),
            (u'test2', u'test2'),
            (u'test-daiwei', u'test-daiwei'),
            (u'press', u'press'),
            (u'dev', u'dev'),
            (u'zft2', u'zft2'),
            (u'xinfutong', u'xinfutong'),
            (u'jinbei', u'jinbei'),
            (u'nuofan', u'nuofan'),
            (u'yisheng', u'yisheng'),
            (u'chuangfu', u'chuangfu'),
            (u'yzf', u'yzf'),
            (u'jicaipay', u'jicaipay'),
            (u'xifpay', u'xifpay'),
            (u'zenxiang', u'zenxiang'),
    )
    SERVER_NAMES = (
            (u'ismp2', u'ismp2'),
            (u'customer', u'customer'),
            (u'notify', u'notify'),
            (u'accounting', u'accounting'),
            (u'acquiring', u'acquiring'),
            (u'agent-manager', u'agent-manager'),
            (u'agent-platform', u'agent-platform'),
            (u'agentPayApi', u'agentPayApi'),
            (u'boss', u'boss'),
            (u'channel-callback', u'channel-callback'),
            (u'channels', u'channels'),
            (u'crontab', u'crontab'),
            (u'ftSecurity', u'ftSecurity'),
            (u'detour', u'detour'),
            (u'eims', u'eims'),
            (u'ismp', u'ismp'),
            (u'mapi', u'mapi'),
            (u'paymentApi', u'paymentApi'),
            (u'settle', u'settle'),
            (u'strategy', u'strategy'),
            (u'reconciliation', u'reconciliation'),
            (u'agentPayCore', u'agentPayCore'),
            (u'riskControl', u'riskControl'),
     )
    created = models.DateTimeField('发布时间', auto_now_add=True)
    version = models.CharField('git_version',max_length = 100)
    servername = models.CharField('应用',max_length = 100,  null=True)
    #product = models.CharField('环境',max_length = 50, choices=PRODUCT_CHOICES, null=True)
    #ip = models.CharField(max_length = 50,default ='-')
    product = models.CharField('环境',max_length = 50,null=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '发布记录'
        ordering = ('created',)
