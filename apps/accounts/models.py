from django.db import models
from apps.permissions.models import User

class Navigation(models.Model):
    name =  models.ForeignKey(User,on_delete=models.CASCADE)
    website_name = models.CharField(max_length=32,verbose_name="网站名字")
    website_url = models.CharField(max_length=256,verbose_name="网站url")
    def __str__(self):
        return self.website_name
    class Meta:
        verbose_name_plural = "网站导航"

