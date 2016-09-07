#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class MySite(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)#博客时间，获取当前时间
    content = models.TextField(blank=True,null=True)

    def ___str__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']
