from django.db import models
from django.conf import settings
#from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as _
#from django.db.models import Max

class Category(models.Model):
    TYPE_CHOICES = (
        (10, _('Father Category')),
        (20, _('Article List')),
        (30, _('Article With Picture List')),
        (40, _('Single Article')),
        (50, _('Link List')),
        (60, _('Redirection Link')),
        (70, _('RSS')),
    )
    name = models.CharField(_('Name'),max_length=30,unique=True)
    icon=models.ImageField(_('Icon'),upload_to=settings.CATEGORY_ICON_PATH,blank=True, null=True,max_length=255)
    type=models.SmallIntegerField(_('Type'),choices=TYPE_CHOICES)
    url=models.URLField(_('URL'),max_length=255,blank=True, null=True,help_text=u'%s, %s'%(_('Redirection Link'),_('RSS')))
#    seqNum=models.IntegerField(_('Serial Number'),default=50,unique=True)
    created=models.DateTimeField(_('Created Time'),auto_now_add=True)
    lastModified=models.DateTimeField(_('Last Modified Time'),auto_now=True)
    father=models.ForeignKey('self',verbose_name=_('Father Category'),blank=True, null=True)
#    tags=models.CharField(_('Tag'),default=' home,',max_length=255,blank=True, null=True)
    appLabel = models.CharField(_('Application Label'),max_length=30,blank=True, null=True)
    description = models.TextField(_('Description'),blank=True, null=True)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        permissions = (
            ("can_admin", "admin for cms module"),
        )
    def __unicode__(self):
        return self.name
    def getIconUrl(self):
        if self.icon:
            return settings.MEDIA_URL+self.icon.url
        else:
            return settings.CATEGORY_DEFAULT_ICON_PATH
    def getName(self):
        return self.name;
    def getUrl(self):
        return '/content/%s/'%self.id
#    def getSeqNum(self):
#        return self.seqNum
    
#def get_category_nex_seq_num():
#    maxNum = Category.objects.all().aggregate(Max('seqNum')).get("seqNum__max",40)
#    if maxNum:
#        return maxNum+10
#    return 50
#
#def get_category_by_tag(page):
#    return Category.objects.filter(tags__contains=' %s,'%page).order_by('-seqNum')
def get_category_by_app_label(app_label):
    l = Category.objects.filter(appLabel__exact=app_label).filter(father__isnull=True)
    assert len(l) <=1,'appLabel repeat.'
    if len(l) == 1:
        return l[0]
    else:
        return None
#def get_father_cateogories():
#    l = Category.objects.filter(type__exact=10)
#    return ((c.id,c.name) for c in l)

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
    pic=models.ImageField(_('Picture'),upload_to=settings.ARTICLE_PIC_PATH,blank=True, null=True,max_length=255)
    type=models.SmallIntegerField(_('Type'),choices=TYPE_CHOICES,editable=False)
    category=models.ForeignKey(Category,verbose_name=_('Category'),editable=False)
    viewTimes=models.BigIntegerField(_('View Times'),default=0,editable=False)
    posted=models.DateTimeField(_('Publish Time'),auto_now_add=True)
    lastModified=models.DateTimeField(_('Last Modified Time'),auto_now=True)
    url=models.URLField(_('URL'),max_length=255,blank=True, null=True)
    setTop=models.SmallIntegerField(_('Set Top'),choices=SET_TOP_CHOICES,default=0)
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        unique_together = ("title", "category")
        permissions = (
        )
    def __unicode__(self):
        return self.title

def get_category_single_article(category_id):
    try:
        return Article.objects.filter(category=category_id).order_by('-setTop','-lastModified')[0]
    except IndexError:
        return None