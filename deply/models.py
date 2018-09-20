from django.db import models, migrations, connection, models

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
    version = models.CharField('git_version',max_length = 100)
    servername = models.CharField('应用',max_length = 100,  null=True)
    #product = models.CharField('环境',max_length = 50, choices=PRODUCT_CHOICES, null=True)
    #ip = models.CharField(max_length = 50,default ='-')
    product = models.CharField('环境',max_length = 50,null=True)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '发布记录'
