from django.db import models
from django.utils.translation import ugettext_lazy as _

class Feedback(models.Model):
    email=models.EmailField(_('Email'),blank=True, null=True)
    referer=models.URLField(_('Referer'),max_length=255,blank=True, null=True,editable=False)
    content=models.TextField(_('Content'))
    read=models.BooleanField(_('Aleady Read'),editable=False,default=False)
    commited=models.DateTimeField(_('Commit Time'),auto_now_add=True)
    commitedIp=models.IPAddressField(_('Commit Ip'),editable=False)
    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
    def __unicode__(self):
        return self.id
            
class SuggestFeature(models.Model):
    name=models.CharField(_('Your Name'),blank=True, null=True,max_length=50)
    email=models.EmailField(_('Email'),blank=True, null=True)
    title = models.CharField(_('Title'),max_length=255)
    content = models.TextField(_('Content'))
    read=models.BooleanField(_('Aleady Read'),editable=False,default=False)
    commited=models.DateTimeField(_('Commit Time'),auto_now_add=True)
    commitedIp=models.IPAddressField(_('Commit Ip'),editable=False)
    class Meta:
        verbose_name = _('Feature Suggest')
        verbose_name_plural = _('Feature Suggest')
    def __unicode__(self):
        return self.id