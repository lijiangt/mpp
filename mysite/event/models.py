from django.db import models

from departments.models import Department

class Event(models.Model):
    CATEGORY_CHOICES = (
        (_('10'), _('News')),
        (_('20'), _('Announcement')),
        (_('30'), _('Bulletin')),
        (_('40'), _('Jobs at Bupt')),
        (_('50'), _('Others')),
    )
    title = models.CharField(_('Title'),max_length=255)
    content = models.TextField(_('Content'))
    date=models.DateTimeField(_('Date'))
    posted=models.DateTimeField(_('Publish Time'),auto_now_add=True)
    lastModified=models.DateTimeField(_('Last Modified Time'),auto_now=True)
    department=models.ForeignKey(Department,verbose_name=_('Department'))
    category=models.CharField(_('Category'),choices=CATEGORY_CHOICES,max_length=255)
    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
    def __unicode__(self):
        return self.title