# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Category(models.Model):
    TYPE_CHOICES = (
        (10, u'父类别'),
        (20, u'文章列表'),
        (30, u'图文列表'),
        (40, u'普通文章列表'),
        (50, u'链接列表'),
        (60, u'跳转链接'),
        (70, u'RSS汇聚'),
    )
    name = models.CharField(u'名称',max_length=30,unique=True)
    icon=models.ImageField(u'图标',upload_to=settings.CATEGORY_ICON_PATH,blank=True, null=True)
    type=models.SmallIntegerField(u'类型',choices=TYPE_CHOICES)
    url=models.CharField(u'链接',max_length=255,blank=True, null=True,help_text=u'跳转链接或者RSS汇聚链接')
    seqNum=models.IntegerField(u'序号',default=1)
    created=models.DateTimeField(u'创建时间',auto_now_add=True)
    lastModified=models.DateTimeField(u'最后修改时间',auto_now=True)
#    father=models.ForeignKey('self',verbose_name=u'父类别')
#排序字段
    tag=models.CharField(u'标签',max_length=255,blank=True, null=True)
    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"

class Article(models.Model):
    TYPE_CHOICES = (
        (10, u'普通'),
        (20, u'图文'),
        (30, u'链接'),        
    )
    SET_TOP_CHOICES = (
        (2, u'置顶'),
        (0, u'普通'),
    )
    title = models.CharField(u'标题',max_length=255)
    content = models.TextField(u'内容')
    pic=models.ImageField(u'图片',upload_to=settings.ARTICLE_PIC_PATH,blank=True, null=True)
    type=models.SmallIntegerField(u'类型',choices=TYPE_CHOICES)
    category=models.ForeignKey(Category,verbose_name=u'类别')
    viewTimes=models.BigIntegerField(u'查看次数',default=0)
    posted=models.DateTimeField(u'发布时间',auto_now_add=True)
    lastModified=models.DateTimeField(u'最后修改时间',auto_now=True)
    setTop=models.SmallIntegerField(u'置顶',choices=SET_TOP_CHOICES)
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        unique_together = ("title", "category")