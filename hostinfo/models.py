from django.db import models


# Create your models here.
class Server(models.Model):
    server_type = ((0, 'PC服务器'),
                   (1, '刀片机'),
                   (2, '小型机'),)
    # 虚拟机专用字段
    IP = models.CharField('IP地址', max_length=30, default='')
    MAC = models.CharField('Mac地址', max_length=200, default='')
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    hostname = models.CharField(max_length=128, null=True, blank=True, verbose_name="主机名")
    os_type = models.CharField('操作系统类型', max_length=64, blank=True, null=True)
    os_distribution = models.CharField('发行商', max_length=64, blank=True, null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"
