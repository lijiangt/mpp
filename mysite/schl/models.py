# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from departments.models import Building
from departments.const import CONST

class School(models.Model):
    """各个院信息"""
    name = models.CharField(_(u'School'),max_length=CONST['namelength'],unique=True)
    description = models.TextField(_(u'Description'),max_length=CONST['description'],null=True,blank=True)
    room = models.CharField(_(u'Room'),max_length=CONST['roomnum'],null=True,blank=True)
    telephone = models.CharField(_(u'Phone'),max_length=CONST['telephone'],null=True,blank=True)
    website = models.URLField(_(u'MainPageUrl'),null=True,blank=True)

    building = models.ForeignKey(Building)
    
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
    
class SubDep(models.Model):
    """院：各个科级信息"""
    name = models.CharField(_(u'Department'),max_length=CONST['namelength'])
    room = models.CharField(_(u'Room'),max_length=CONST['roomnum'],null=True,blank=True)
    telephone = models.CharField(_(u'Phone'),max_length=CONST['telephone'],null=True,blank=True)

    building = models.ForeignKey(Building)
    school = models.ForeignKey(School)
 
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
