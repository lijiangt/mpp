from models import Category

class CmsProvider(object):
    def __init__(self,**kwargs):
        self.kwargs = kwargs;
        self.page = kwargs['page']
        
    def getApps(self):
        return Category.objects.filter(tags__contains=',%s,'%self.page).order_by('-seqNum')