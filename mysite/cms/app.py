from models import get_category_by_app_label

class CmsApp(object):
    def __init__(self,**kwargs):
        self.kwargs = kwargs;
        app_label = kwargs.get('app_label',None)
        assert app_label,'CmsApp class requires app_label kwargs argument.'
        category = get_category_by_app_label(app_label)
        if category:
            self.iconUrl = category.getIconUrl()
            self.name = category.getName()
            self.url = category.getUrl()
        else:
            self.iconUrl = None
            self.name = None
            self.url = None
    
    def getIconUrl(self):
        return self.iconUrl
    def getName(self):
        return self.name
    def getUrl(self):
        return self.url