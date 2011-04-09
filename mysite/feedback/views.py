from django import forms
from django.shortcuts import HttpResponseRedirect,  render_to_response
from django.template import RequestContext
from models import SuggestFeature, Feedback

import urllib

class SuggestFeatureForm(forms.ModelForm):
    ref=forms.URLField(widget=forms.HiddenInput(),max_length=255,required=False)
    class Meta:
        model = SuggestFeature


def feature_suggestions(request):
    if request.method == 'GET':
        referer = request.META.get('HTTP_REFERER','/')
        f = SuggestFeatureForm(initial={'ref': referer})
        return render_to_response('feedback/feature_suggestions_form.html', {
                'form':            f,
#                "submit_times":   -1,
#                'display_cancel':'true',
                'referer':referer,
        },context_instance=RequestContext(request))
    elif request.method == 'POST':
        f = SuggestFeatureForm(request.POST)
        if f.is_valid():
            referer = request.POST.get('ref','')
            sf = f.save(commit=False)
            sf.commitedIp = request.META.get('REMOTE_ADDR','')
            sf.save()
            return HttpResponseRedirect('./result?id=%s&next=%s'%(sf.id,urllib.quote_plus(referer)))
        else:
            referer = request.POST.get('ref','/')
            return render_to_response('feedback/feature_suggestions_form.html', {
                    'form':        f,
#                    "submit_times":int(request.POST['submit_times']) - 1,
#                    'display_cancel':request.POST.get('display_cancel','true'),
                    'referer':referer,
                    },context_instance=RequestContext(request))

def feature_suggestions_result(request):
    return render_to_response('feedback/feature_suggestions_result.html', {
                    'id':request.GET.get('id',''),
                    'next':request.GET.get('next','/'),
                    },context_instance=RequestContext(request))

class FeedbackForm(forms.ModelForm):
    ref=forms.URLField(widget=forms.HiddenInput(),max_length=255,required=False)
    class Meta:
        model = Feedback
        exclude = ('referer',)
        
def feedback(request):
    if request.method == 'GET':
        referer = request.META.get('HTTP_REFERER','/')
        f = FeedbackForm(initial={'ref': referer})
        return render_to_response('feedback/feedback_form.html', {
                'form':            f,
#                "submit_times":   -1,
#                'display_cancel':'true',
                'referer':referer,
        },context_instance=RequestContext(request))
    elif request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            feedback = f.save(commit=False)
            feedback.commitedIp = request.META.get('REMOTE_ADDR','')
            feedback.referer = request.POST.get('ref','')
            feedback.save()
            return HttpResponseRedirect('./result?id=%s&next=%s'%(feedback.id,urllib.quote_plus(feedback.referer)))
        else:
            referer = request.POST.get('ref','/')
            return render_to_response('feedback/feedback_form.html', {
                    'form':        f,
#                    "submit_times":int(request.POST['submit_times']) - 1,
#                    'display_cancel':request.POST.get('display_cancel','true'),
                    'referer':referer,
                    },context_instance=RequestContext(request))

def feedback_result(request):
    return render_to_response('feedback/feedback_result.html', {
                    'id':request.GET.get('id',''),
                    'next':request.GET.get('next','/'),
                    },context_instance=RequestContext(request))