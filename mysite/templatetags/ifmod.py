from django import template

register = template.Library()

class IfModNode(template.Node):
    def __init__(self, nodelist, para1, para2,para3):
        self.nodelist = nodelist
        self.para1 = template.Variable(para1)
        self.para2 = template.Variable(para2)
        self.para3 = template.Variable(para3)
    def render(self, context):
        if (int(self.para1.resolve(context)))%(int(self.para2.resolve(context)))==int(self.para3.resolve(context)):
            return self.nodelist.render(context)
        else:
            return ''

@register.tag
def ifmod(parser, token):
    nodelist = parser.parse(('endifmod',))
    print nodelist
    print token
    parser.delete_first_token()
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, para1, para2, para3 = token.split_contents()
        return IfModNode(nodelist,para1, para2, para3)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires three arguments" % tag_name
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