from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _

class Page(object):
    def __init__(self,local_name_key,title,providers,**kwargs):
        self.title,self.providers = title,providers
        self.kwargs = kwargs
        self.local_name = _(local_name_key)
        
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

