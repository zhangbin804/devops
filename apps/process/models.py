from django.db import models
from apps.permissions.models import User



class Process(models.Model):
    user = models.ManyToManyField(User,through="Intermediate")
    name = models.CharField(max_length=64,verbose_name="流程表名字")
    process = models.CharField(max_length=256,verbose_name="流程")
    describe = models.CharField(max_length=512,verbose_name="描述")
    create_time = models.CharField(max_length=128,verbose_name="创建时间")
    change_time = models.CharField(max_length=128,verbose_name="修改时间",default='',null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "流程表"

class Intermediate(models.Model):
    create_user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=64,verbose_name="流程名",default='test')
    process = models.ForeignKey(to="Process",on_delete=models.CASCADE)
    describe = models.CharField(max_length=512,verbose_name="申请描述",default='',null=True)
    attachment = models.CharField(max_length=512,verbose_name="附件",default='',null=True)
    process_str = models.CharField(max_length=256, verbose_name="流程")
    user = models.CharField(max_length=8,verbose_name="审核人",default=None,)
    create_time = models.CharField(max_length=128,verbose_name="创建时间",default='',null=True)
    status = models.CharField(max_length=8,choices=(('0','审核中'),('1','审核拒绝'),('2','审核通过')),default='0')
    is_read = models.IntegerField(choices=((0,'未查看'),(1,'已查看')),default=0,verbose_name='是否查看')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "流程创建与审核"


