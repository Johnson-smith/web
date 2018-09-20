from django.db import models, migrations

# Create your models here.

class Host(models.Model):
    GENDER_CHOICES = (
            (u'yifudev', u'yifudev'),
            (u'paywotrh', u'paywotrh'),
            (u'fsxy996', u'fsxy996'),
            (u'北京兴荣利泰贸易有限公司', u'北京兴荣利泰贸易有限公司'),
            (u'18676858470', u'18676858470'),
            (u'若凡信息科技', u'若凡信息科技'),
            (u'wepay3@easypay', u'wepay3@easypay'),
            (u'wpccoy89', u'wpccoy89'),
            (u'cheespay', u'cheespay'),
            (u'idc', u'idc'),
            (u'温州祯祥', u'温州祯祥'),
            (u'caijipay', u'caijipay'),
            (u'xifpay', u'xifpay'),
    )
    PRODUCT_CHOICES = (
            (u'wanliu-prod', u'wanliu-prod'),
            (u'wanliu-test', u'wanliu-test'),
            (u'wanliu-press', u'wanliu-press'),
            (u'wanliu-dev', u'wanliu-dev'),
            (u'wanliu-devops', u'wanliu-devops'),
            (u'zft', u'zft'),
            (u'zft-2', u'zft-2'),
            (u'xingfutong', u'xingfutong'),
            (u'jinbei', u'jinbei'),
            (u'nuofan', u'nuofan'),
            (u'yisheng', u'yisheng'),
            (u'chuangfu', u'chuangfu'),
            (u'yzf', u'yzf'),
            (u'吉财', u'吉财'),
            (u'喜付', u'喜付'),
    )
    MEMROY_CHOICES = (
            (u'M', u'2G'),
            (u'G', u'4G'),
            (u'H', u'8G'),
            (u'J', u'16G'),
            (u'K', u'32G'),
    )
    product = models.CharField('环境',max_length = 50)
    hostname = models.CharField('机器名',max_length = 50)
    publicip = models.CharField('入口公网ip',max_length = 50,default ='-')
    publicip1 = models.CharField('对外公网ip',max_length = 50,default ='-')
    privateip = models.GenericIPAddressField('私网ip', null=True, blank=True)
    #processor_cores = models.CharField('cpu_num',max_length = 50, null=True)
    cpu_num = models.CharField(max_length = 50,default ='-')
    gateway = models.CharField(blank=True,max_length = 50)
    mac = models.CharField(blank=True,max_length = 50)
    distribution = models.CharField(blank=True,max_length = 50)
    distribution_version = models.CharField(blank=True,max_length = 50)
    architecture = models.CharField(blank=True,max_length = 50)
    kernel = models.CharField(blank=True,max_length = 50)
    processor = models.CharField(blank=True,max_length = 50)
    processor_count = models.CharField(blank=True,max_length = 50)
    #processor = models.IntegerField('cpu_core')
    #memory = models.CharField(max_length = 50, choices=MEMROY_CHOICES)
    memory = models.CharField(max_length = 50)
    app_name = models.CharField('应用名',max_length = 100)
    #account = models.CharField('云账号',max_length = 50, choices=GENDER_CHOICES,default = '-')
    account = models.CharField('云账号',max_length = 50,default = '-')
    class Meta:
        verbose_name = '机器'
        verbose_name_plural = '机器'