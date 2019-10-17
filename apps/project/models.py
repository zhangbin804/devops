from django.db import models
from apps.permissions.models import User,Role
from apps.operational.models import Group


class Project(models.Model):
    title = models.CharField(max_length=64,blank=False,unique=True,verbose_name="项目名")
    create_time = models.CharField(max_length=32,default='',blank=True,null=True,verbose_name="创建时间")
    change_time = models.CharField(max_length=32,default='',blank=True,null=True,verbose_name="上次部署时间")
    create_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='创建人')
    describe = models.CharField(max_length=512,default='',blank=True,null=True,verbose_name="描述")
    server_group = models.ForeignKey(Group,on_delete=models.CASCADE,verbose_name='上线服务器组')
    git_url = models.CharField(max_length=128,default='',blank=True,null=True,verbose_name="git url")
    git_auth_way = models.IntegerField(choices=((0,'账号密码认证'),(1,'已ssh-key认证')),verbose_name='认证方式')
    git_user = models.CharField(max_length=16,default='',blank=True,null=True,verbose_name='git认证账号')
    git_password = models.CharField(max_length=64,default='123456',blank=True,null=True,verbose_name='git认证密码')
    git_branch = models.CharField(max_length=16,default='',blank=False,verbose_name='分支')
    deploy_dir = models.CharField(max_length=512,null=False,blank=False)
    exclude_file = models.CharField(max_length=4096,default='',blank=True,null=True,verbose_name='排除文件')
    online_notice = models.CharField(max_length=16,choices=(('email','邮件'),('dingding','钉钉')),default='email',verbose_name='通知方式')
    email_notice = models.ForeignKey(Role,default='',blank=True,null=True,on_delete=models.CASCADE,verbose_name='邮件通知的组')
    dingding_notice = models.CharField(max_length=128,default='',blank=True,null=True,verbose_name='钉钉通知地址')
    work_dir = models.CharField(max_length=128,null=True,blank=True,verbose_name='git clone所在目录')
    connection_auth = models.IntegerField(default=0,choices=((0,'未连接测试'),(1,'连接失败'),(2,'连接成功')))
    log = models.ForeignKey(to="Log",blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "项目"


class Log(models.Model):
    git_tag = models.CharField(max_length=64,blank=False,verbose_name='git tag版本')
    git_commit = models.CharField(max_length=256,blank=False,verbose_name='git commit版本')
    text = models.CharField(max_length=10240,verbose_name='日志文本')
    new_time = models.CharField(max_length=18,blank=False,verbose_name='操作时间')
    operation_user = models.CharField(max_length=18,verbose_name='操作人')
    on_version_log_id = models.IntegerField(blank=True,null=True,verbose_name='上个版本日志id')
    count_num = models.IntegerField(blank=True,null=True,verbose_name='次数')
  
    def __str__(self):
        return self.git_commit
    class Meta:
        verbose_name_plural = "项目日志"

