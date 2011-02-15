from models import get_category_by_tag

class CmsProvider(object):
    def __init__(self,**kwargs):
        self.kwargs = kwargs;
        self.page = kwargs['page']
        
    def getApps(self):
        return get_category_by_tag(self.page)