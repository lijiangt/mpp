from django import template

register = template.Library()
ALREADY_INCLUDE_JS_VARIABLE = 'already_include_js'

class JsIncludeNode(template.Node):
    def __init__(self, nodelist, js_lib_name,update_variable):
        self.nodelist = nodelist
        self.js_lib_name = js_lib_name
        self.update_variable = update_variable
    def render(self, context):
        already_include = context.get(ALREADY_INCLUDE_JS_VARIABLE,None)
        if already_include == None:
            already_include = []
        if self.js_lib_name not in already_include:
            if self.update_variable:
                already_include.append(self.js_lib_name)
                context[ALREADY_INCLUDE_JS_VARIABLE]=already_include
            return self.nodelist.render(context)
        else:
            return ''

@register.tag
def jsinclude(parser, token):
    nodelist = parser.parse(('endjsinclude',))
    parser.delete_first_token()
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, js_lib_name = token.split_contents()
        return JsIncludeNode(nodelist,js_lib_name,False)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires one arguments" % tag_name
@register.tag
def jsincludeorigin(parser, token):
    nodelist = parser.parse(('endjsincludeorigin',))
    parser.delete_first_token()
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, js_lib_name = token.split_contents()
        return JsIncludeNode(nodelist,js_lib_name,True)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires one arguments" % tag_name
    
#    
#    
#    
#    paras = token.split_contents()
#    num = len(paras)
#    print paras
#    if num==3:
#        return IfModNode(nodelist,(int(paras[1]))%(int(paras[2]))==0);
#    elif num==4:
#        return IfModNode(nodelist,(int(paras[1]))%(int(paras[2]))==(int(paras[3])))
#    else:
#        raise template.TemplateSyntaxError, "%r tag requires two or three argument" % paras[0]    