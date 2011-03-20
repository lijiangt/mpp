# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from const import CONST

class Building(models.Model):
    """学校各个教学楼等"""
    name = models.CharField(_(u'Building'),max_length=CONST['namelength'],unique=True)
    description = models.TextField(_(u'Description'),max_length=CONST['description'],null=True,blank=True)
    latitude = models.FloatField(_(u'Latitude'),null=True,blank=True)
    atitude = models.FloatField(_(u'Atitude'),null=True,blank=True)
    
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Department(models.Model):
    """学校各个处级信息"""
    name = models.CharField(_(u'Department'),max_length=CONST['namelength'],unique=True)
    description = models.TextField(_(u'Description'),max_length=CONST['description'],null=True,blank=True)
    room = models.CharField(_(u'Room'),max_length=CONST['roomnum'],null=True,blank=True)
    telephone = models.CharField(_(u'Phone'),max_length=CONST['telephone'],null=True,blank=True)
    worktime = models.CharField(_(u'WorkTime'),default='上午8:30到11:30,下午1:30到5:00',max_length=CONST['worktime'],null=True,blank=True)
    website = models.URLField(_(u'MainPageUrl'),null=True,blank=True)

    building = models.ForeignKey(Building)
    
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
    
class SubDepartment(models.Model):
    """各个处中的科级信息"""
    name = models.CharField(_(u'SubDepartment'),max_length=CONST['namelength'])
    room = models.CharField(_(u'Room'),max_length=CONST['roomnum'],null=True,blank=True)
    telephone = models.CharField(_(u'Phone'),max_length=CONST['telephone'],null=True,blank=True)

    building = models.ForeignKey(Building)
    department = models.ForeignKey(Department)
 
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
