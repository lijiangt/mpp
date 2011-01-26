from django.utils.importlib import import_module

class Page(object):
    def __init__(self,title,providers,**kwargs):
        self.title,self.providers = title,providers
        self.kwargs = kwargs
        
    def getApps(self):
        apps = []
        for provider in self.providers:
            apps.extend(provider.getApplications());
        # TODO reorder
        return apps

class Provider(object):
    def __init__(self, cls, **kwargs):
        self.cls, self.kwargs = cls, kwargs

    def getApplications(self):
        mod_name, cls_name = self.cls.rsplit('.', 1)
        module = import_module(mod_name)
        cls = getattr(module, cls_name)
        return cls(**self.kwargs).getApps()

