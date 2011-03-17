# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

DEFAULT_VALUE = {
                     'worktime':'from 8:30 to 11:30 & from 13:30 to 17:00',
                     'namelength':20,#包括：楼名，处名，科名，人名
                     'description':200,
                     'roomnum':8,
                     'telephone':12,
                     'idnum':18,
                     }
    
class Building(models.Model):
    """学校各个教学楼等"""
    name = models.CharField(_(u'Building'),max_length=DEFAULT_VALUE['namelength'],unique=True)
    description = models.TextField(_(u'Description'),max_length=DEFAULT_VALUE['descroption'],null=True,blank=True)
    latitude = models.FloatField(_(u'Latitude'),null=True,blank=True)
    atitude = models.FloatField(_(u'Atitude'),null=True,blank=True)
    
    def __unicode__(self):
        return self.name

class Department(models.Model):
    """学校各个处级信息"""
    name = models.CharField(_(u'Department'),max_length=['namelength'],unique=True)
    description = models.TextField(_(u'Description'),max_length=DEFAULT_VALUE['descroption'],null=True,blank=True)
    room = models.CharField(_(u'Room'),max_length=['roomnum'],null=True,blank=True)
    telephone = models.CharField(_(u'Phone'),max_length=32,null=True,blank=True)
    worktime = models.CharField(_(u'WorkTime'),null=True,blank=True)
    website = models.URLField(_(u'MainPageUrl'),null=True,blank=True)

    building = models.ForeignKey(Building)
    
    def __init__(self):
        self.worktime = DEFAULT_VALUE['worktime']
    
    def __unicode__(self):
        return self.name
    
class SmallDepartment(models.Model):
    """各个处中的科级信息"""
    name = models.CharField(_(u'Department'),max_length=['namelength'])
    room = models.CharField(_(u'Room'),max_length=DEFAULT_VALUE['roomnum'],null=True,blank=True)
    telephone = models.CharField(_(u'Phone'),max_length=DEFAULT_VALUE['telephone'],null=True,blank=True)
    building = models.CharField(_(u'Building'),max_length=DEFAULT_VALUE['namelength'])

    department = models.ForeignKey(Department)
    
    def __init__(self):
        self.building = self.department.building  #默认情况下，一个职能处在同一个楼
 
    def __unicode__(self):
        return u'%s:%s'(Department.name,self.name)