from django.db import models

# Create your models here.


class Server(models.Model):
    server_name = models.CharField(max_length=32,unique=True,verbose_name='服务器名')
    ip = models.CharField(max_length=15,unique=True,verbose_name='ip地址')
    user = models.CharField(max_length=12,null=True,verbose_name='ssh账号')
    password = models.CharField(max_length=32,null=True,verbose_name='ssh密码')
    # ssh_key = models.CharField(max_length=2048,verbose_name='ssh-key私钥')
    port = models.IntegerField(null=True,verbose_name='ssh端口')
    groups = models.ManyToManyField(to="Group",verbose_name="组内的服务器",blank=True)
    status = models.CharField(max_length=4,verbose_name='状态',choices=(('0','未认证'),('1','已认证')),default='0')
    def __str__(self):
        return self.server_name
    class Meta:
        verbose_name_plural = "服务器"


class Group(models.Model):
    title = models.CharField(max_length=32,unique=True,verbose_name="组名称")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "服务器组"



class ServerUser(models.Model):
    username = models.CharField(max_length=32,unique=True,verbose_name='ssh账号')
    password = models.CharField(max_length=32,verbose_name='ssh密码')
    senior = models.IntegerField(default=0,choices=((0,'空'),(1,'有选择')))
    uid = models.IntegerField(null=True,blank=True,verbose_name='uid')
    gid = models.IntegerField(null=True,blank=True,verbose_name='gid')
    sudo = models.CharField(null=True,blank=True,max_length=1024,verbose_name='sudo权限')
    create_time = models.CharField(max_length=32,verbose_name='创建时间',null=True)
    way = models.IntegerField(default=0,choices=((0,'空'),(1,'server'),(2,'group')))
    servers = models.ManyToManyField(to='Server',verbose_name="服务器",blank=True)
    groups = models.ManyToManyField(to='Group',verbose_name="服务器组",blank=True)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "服务器ssh账号"
