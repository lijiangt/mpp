from django import forms

from const import CONST

class BuildingForm(forms.Form):
    name = forms.CharField(_(u'Building'),max_length=CONST['namelength'],unique=True)
    description = forms.CharField(_(u'Description'),max_length=CONST['description'],required=False,widget=forms.Textarea)
    latitude = forms.FloatField(_(u'Latitude'),required=False)
    longitude = forms.FloatField(_(u'Longitude'),required=False)


class DeparmentForm(forms.Form):
    name = forms.CharField(_(u'Department'),max_length=CONST['namelength'],unique=True)
    description = forms.CharField(_(u'Description'),max_length=CONST['description'],required=False,widget=forms.Textarea)
    room = forms.CharField(_(u'Room'),max_length=CONST['roomnum'],required=False)
    telephone = forms.CharField(_(u'Phone'),max_length=CONST['telephone'],required=False)
    worktime = forms.CharField(_(u'WorkTime'),max_length=CONST['worktime'],required=False)
    website = forms.URLField(_(u'MainPageUrl'),required=False)
    
class SubDepartmentForm(forms.Form):
    name = forms.CharField(_(u'Department'),max_length=CONST['namelength'])
    room = forms.CharField(_(u'Room'),max_length=CONST['roomnum'],required=False)
    telephone = forms.CharField(_(u'Phone'),max_length=CONST['telephone'],required=False)
    building = forms.CharField(_(u'Building'),max_length=CONST['namelength'])