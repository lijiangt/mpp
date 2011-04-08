from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _

class Page(object):
    def __init__(self,local_name_key,providers,**kwargs):
        self.providers = providers
        self.kwargs = kwargs
        self.local_name = _(local_name_key)
        
    def getApps(self):
        apps = []
        for provider in self.providers:
            app = provider.getApplication()
            if app and app.getName():
                apps.append(app)
#            apps.extend(provider.getApplications());
#        apps.sort(lambda x,y: cmp(x.getSeqNum(), y.getSeqNum()))
        return apps

class Provider(object):
    def __init__(self, cls, **kwargs):
        self.cls, self.kwargs = cls, kwargs

    def getApplication(self):
        mod_name, cls_name = self.cls.rsplit('.', 1)
        module = import_module(mod_name)
        cls = getattr(module, cls_name)
        return cls(**self.kwargs)
    
class GenericApp(object):
    def __init__(self,**kwargs):
        self.iconUrl = kwargs['iconUrl']
        self.url = kwargs['url']
        local_name = kwargs.get('local_name',None)
        if local_name:
            self.name = _(local_name)
        else:
            self.name = kwargs['name']
                
    def getIconUrl(self):
        return self.iconUrl
    def getName(self):
        return self.name
    def getUrl(self):
        return self.url
            
            

