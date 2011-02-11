# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.utils.translation import ugettext
from django.utils.encoding import force_unicode
import theme

ORDER_FIELD_PARA='sort'
DEFAULT_ASC_ORDER = True

register = template.Library()
def get_url(para):
    str = ''
    for item in para.items():
        if str:
            str += '&amp;%s=%s'%(item[0],item[1])
        else:
            str += '?%s=%s'%(item[0],item[1])
    return str

def get_order_str(request):
    para = request.GET
    field = para.get(ORDER_FIELD_PARA,None)
    if field:
        return field
    else:
        return None
    
class TagNode(template.Node):
    def __init__(self,field,name_key,current_asc=None):
        self.field = field
        self.name_key = name_key
        self.current_asc = current_asc
        
    def render(self, context):
        para = context['request'].GET.copy()
        field = self.field.resolve(context)
        name = force_unicode(ugettext(self.name_key.resolve(context)))
        sort = para.get(ORDER_FIELD_PARA,None)
        if (sort and (field == sort or '-'+field == sort)) or (not sort and self.current_asc != None):
            if para.has_key(ORDER_FIELD_PARA):
                asc = True
                if para.get(ORDER_FIELD_PARA).startswith('-'):
                    asc = False
            elif not para.has_key(ORDER_FIELD_PARA) and self.current_asc != None:
                asc = self.current_asc
            if asc:
                para[ORDER_FIELD_PARA]='-'+field
            else:
                para[ORDER_FIELD_PARA]=field
            reverse_order_name=force_unicode('正向')
            order_alt = force_unicode('降序 ')
            order = 'desc'
            if asc:
                order = 'asc'
                reverse_order_name=force_unicode('反向')
                order_alt = force_unicode('升序 ')
            return force_unicode('<a href="%(url)s" title="点击此处按%(name)s%(reverse_order_name)s排序">\
%(name)s<img src="%(media_url)s/themes/%(theme)s/button/sort_%(order)s.gif" alt="降序">\
</a>')%{'url':get_url(para),
                     'name':name,
                     'reverse_order_name':reverse_order_name,
                     'media_url':settings.MEDIA_URL,
                     'theme':theme.ThemeNode().render(context),
                     'order':order,
                     'order_alt':order_alt,
                     }
        else:
            if DEFAULT_ASC_ORDER:
                para[ORDER_FIELD_PARA]=field
            else:
                para[ORDER_FIELD_PARA]='-'+field
            return force_unicode('<a href="%(url)s" title="点击此处按%(name)s%(order_name)s排序">%(name)s</a>')%{'url':get_url(para),
                         'name':name,
                         'order_name':force_unicode('正向')}

@register.tag
def title_field_html(parser, token):
    paras = token.split_contents()
#    print paras
    if len(paras) == 4:
        if paras[3] in ['+','-']:
            return TagNode(parser.compile_filter(paras[1]),parser.compile_filter(paras[2]),paras[3]=='+')
        else:
            raise template.TemplateSyntaxError, "%r tag argument must be '+' or '-'" % paras[0]
    elif len(paras) == 3:
        return TagNode(parser.compile_filter(paras[1]),parser.compile_filter(paras[2]))
    else:
        raise template.TemplateSyntaxError, "%r tag requires two or three arguments" % paras[0]    
