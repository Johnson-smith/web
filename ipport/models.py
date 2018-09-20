from django.db import models

# Create your models here.
class Yinshe(models.Model):
    publicip = models.CharField('公网ip',max_length = 100)
    publicip_port = models.CharField('公网端口',max_length = 100,  null=True)
    parviteip = models.CharField('内网ip',max_length = 100)
    parviteip_port = models.CharField('内网端口',max_length = 100,  null=True)
    product = models.CharField('环境',max_length = 50,  null=True)
    Agreement = models.CharField('协议',max_length = 50,  null=True)
    class Meta:
        verbose_name = '端口映射表'
        verbose_name_plural = '端口映射表'