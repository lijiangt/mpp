from django.db import models
from django.conf import settings
#from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    TYPE_CHOICES = (
#        (10, _('Father Category')),
        (20, _('Article List')),
        (30, _('Article With Picture List')),
        (40, _('Single Article')),
        (50, _('Link List')),
        (60, _('Redirection Link')),
        (70, _('RSS')),
    )
    name = models.CharField(_('Name'),max_length=30,unique=True)
    icon=models.ImageField(_('Icon'),upload_to=settings.CATEGORY_ICON_PATH,blank=True, null=True)
    type=models.SmallIntegerField(_('Type'),choices=TYPE_CHOICES)
    url=models.URLField(_('URL'),max_length=255,blank=True, null=True,help_text=u'%s, %s'%(_('Redirection Link'),_('RSS')))
    seqNum=models.IntegerField(_('Serial Number'),default=50,unique=True)
    created=models.DateTimeField(_('Created Time'),auto_now_add=True)
    lastModified=models.DateTimeField(_('Last Modified Time'),auto_now=True)
#    father=models.ForeignKey('self',verbose_name=_('Father Category'))
    tags=models.CharField(_('Tag'),default=',home,',max_length=255,blank=True, null=True)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')
    def __unicode__(self):
        return self.name
    def getIconUrl(self):
        return self.icon.url
    def getName(self):
        return self.name;
    def getUrl(self):
        return '/content/%s/'%self.id
    def getSeqNum(self):
        return self.seqNum

class Article(models.Model):
    TYPE_CHOICES = (
        (10, _('Normal')),
        (20, _('Article With Picture')),
        (30, _('Friend Link')),        
    )
    SET_TOP_CHOICES = (
        (2, _('Set Top')),
        (0, _('Normal')),
    )
    title = models.CharField(_('Title'),max_length=255)
    content = models.TextField(_('Content'))
    pic=models.ImageField(_('Picture'),upload_to=settings.ARTICLE_PIC_PATH,blank=True, null=True)
    type=models.SmallIntegerField(_('Type'),choices=TYPE_CHOICES)
    category=models.ForeignKey(Category,verbose_name=_('Category'),editable=False)
    viewTimes=models.BigIntegerField(_('View Times'),default=0,editable=False)
    posted=models.DateTimeField(_('Publish Time'),auto_now_add=True)
    lastModified=models.DateTimeField(_('Last Modified Time'),auto_now=True)
    setTop=models.SmallIntegerField(_('Set Top'),choices=SET_TOP_CHOICES,default=0)
    url=models.URLField(_('URL'),max_length=255,blank=True, null=True)
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Article')
        unique_together = ("title", "category")
    def __unicode__(self):
        return self.title
