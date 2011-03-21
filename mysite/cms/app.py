from models import get_category_by_app_label

class CmsApp(object):
    def __init__(self,**kwargs):
        self.kwargs = kwargs;
        app_label = kwargs.get('app_label',None)
        assert app_label,'CmsApp class requires app_label kwargs argument.'
        self.category = get_category_by_app_label(app_label)
    
    def getIconUrl(self):
        if self.category:
            return self.category.getIconUrl()
        else:
            return None
    def getName(self):
        print self.category
        if self.category:
            return self.category.getName()
        else:
            return None
    def getUrl(self):
        if self.category:
            return self.category.getUrl()
        else:
            return None