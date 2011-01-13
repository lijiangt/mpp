# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Category(models.Model):
    TYPE_CHOICES = (
        (10, u'父频道'),
        (20, u'文章列表'),
        (30, u'图文列表'),
        (40, u'普通文章列表'),
        (50, u'链接列表'),
        (60, u'跳转链接'),
        (70, u'RSS汇聚'),
    )
    name = models.CharField(u'名称',max_length=30)
    icon=models.ImageField(u'图标',upload_to=settings.CATEGORY_ICON_PATH)
    type=models.SmallIntegerField(u'类型',choices=TYPE_CHOICES)
    url=models.CharField(u'链接',max_length=255)

class Article(models.Model):
    TYPE_CHOICES = (
        (10, u'普通'),
        (20, u'图文'),
        (30, u'链接'),        
    )
    title = models.CharField(u'标题',max_length=30)
    content = models.TextField(u'内容')
    pic=models.ImageField(u'图片',upload_to=settings.ARTICLE_PIC_PATH,blank=True, null=True)
    type=models.SmallIntegerField(u'类型',choices=TYPE_CHOICES)
    category=models.ForeignKey('Category',verbose_name=u'频道')
    viewTimes=models.BigIntegerField(u'查看次数',default=0)
