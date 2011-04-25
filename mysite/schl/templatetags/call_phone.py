# -*- coding: utf-8 -*-


from django import template
from django.conf import settings

PHONES = {'iPhone':'tel:',
          'Android':'wtai://wp/mc;',}

if settings.DEBUG:
    PHONES['Macintosh']='tel:'
"""
iPhone - Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3
2
iTouch - Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A100a Safari/419.3
3
Android - Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522+ (KHTML, like Gecko) Safari/419.3
4
Palm Pre - Mozilla/5.0 (webOS/1.0; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Pre/1.0
    sms:<phone_number>[,<phone-number>]*[?body=<message_body>]
    
     地图定位GPS
              'iPhone':' <a href="callto:[phone_number]">phone_number</a>',
              'anDroid':' <a href="wtai://wp/mc;[phone_number]">phone_number</a>',
    
        <a href="geopoint:[经度],[纬度]">我的位置</a>
    例如：
    
        <a href="geopoint:100,23">我的位置</a>
        9. Mail 邮件
    
    就和普通的html一样使用mailto
    
       <a href="mailto:nobody@wordpress.com"></a>
       <a href="mailto:nobody@wordpress.com,no.one@wordpress.com"></a>
       <a href="mailto:nobody@wordpress.com?subject=Testing"></a>
       <a href="mailto:nobody@wordpress.com?subject=Testing mailto&cc=no.one@wrodpress.com"></a>
#        (context['request'].META['HTTP_USER_AGENT'].
       
"""
DEFAULT_ZONE_NUM = '010' #not a good method ,just for now
register = template.Library()

class PhoneNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
            
    def render(self, context):
#        output = context['request'].META['HTTP_USER_AGENT'] #self.nodelist.render(context).META['HTTP_USER_AGENT']
        browser = context['request'].META.get('HTTP_USER_AGENT')
        output = self.nodelist.render(context)
        for k,v in PHONES.items():
            if browser.find(k)>0:
                return '<a href="%s%s%s">%s</a>'%(v,DEFAULT_ZONE_NUM,output,output)#find phone 
        return '%s' % output    
    
@register.tag
def call_phone(parser, token):
    nodelist = parser.parse(('endcall_phone',))
    parser.delete_first_token()
    return PhoneNode(nodelist)