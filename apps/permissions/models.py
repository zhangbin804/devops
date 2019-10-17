from django.db import models

class Role(models.Model):
    title = models.CharField(max_length=32,verbose_name="角色")
    permissions = models.ManyToManyField(to="Permission",verbose_name="拥有权限的角色",blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "角色表"

class Permission(models.Model):
    title = models.CharField(max_length=32,verbose_name="权限名")
    url = models.CharField(max_length=64,verbose_name="带正则的url")
    codes = models.CharField(max_length=32,verbose_name="代码")
    group = models.ForeignKey(to="Group",verbose_name="所属组",on_delete=models.CASCADE,blank=True)
    menu_gp = models.ForeignKey(to='Permission',related_name='aaa',on_delete=models.CASCADE,null=True,blank=True,verbose_name="组内菜单")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "权限表"

class User(models.Model):
    name = models.CharField(max_length=32,verbose_name="账号名")
    username = models.CharField(max_length=32,verbose_name="真实姓名",unique=True)
    password = models.CharField(max_length=64,verbose_name="密码")
    email = models.CharField(max_length=32,verbose_name="邮箱")
    head_img = models.CharField(max_length=512,verbose_name="头像",default="static/avatar/default_avatar.jpg")
    create_time = models.CharField(max_length=64,verbose_name="创建时间")
    disable = models.IntegerField(choices=((0,'启用'),(1,'禁用')),default=0)
    roles = models.ManyToManyField(to="Role",blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "用户表"

class Group(models.Model):
    title = models.CharField(max_length=32,verbose_name="组名称")
    menu = models.ForeignKey(to="Menu",verbose_name="组内菜单",on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "组"

class Menu(models.Model):
    caption = models.CharField(max_length=32,verbose_name="菜单")
    def __str__(self):
        return self.caption
    class Meta:
        verbose_name_plural = "菜单表"
