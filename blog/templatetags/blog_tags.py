from django.utils.safestring import mark_safe
from mptt.templatetags.mptt_tags import cache_tree_children
from django.utils.translation import ugettext as _
from django import template


register = template.Library()


class RecurseTreeNode(template.Node):
    def __init__(self, template_nodes, queryset_var):
        self.template_nodes = template_nodes
        self.queryset_var = queryset_var

    def _render_node(self, context, node, length=0, index=0):
        bits = []
        context.push()
        for child in node.get_children():
            bits.append(self._render_node(context, child))
        #将index添加到上下文里，和forloop一样，也提供四种计数方式
        context['counter'] = index + 1
        context['counter0'] = index
        context['revcounter'] = length - index
        context['revcounter0'] = length - index - 1
        context['node'] = node
        context['children'] = mark_safe(''.join(bits))
        rendered = self.template_nodes.render(context)
        context.pop()
        return rendered

    def render(self, context):
        queryset = self.queryset_var.resolve(context)
        roots = cache_tree_children(queryset)
        bits = []
        #通过enumerate，获取当前的index
        for index, node in enumerate(roots):
            bits.append(self._render_node(context, node, len(roots), roots.index(node)))
        return ''.join(bits)


@register.tag
def recursetree(parser, token):
    """
    Iterates over the nodes in the tree, and renders the contained block for each node.
    This tag will recursively render children into the template variable {{ children }}.
    Only one database query is required (children are cached for the whole tree)
    Usage:
            <ul>
                {% recursetree nodes %}
                    <li>
                        {{ node.name }}
                        {% if not node.is_leaf_node %}
                            <ul>
                                {{ children }}
                            </ul>
                        {% endif %}
                    </li>
                {% endrecursetree %}
            </ul>
    """
    bits = token.contents.split()
    if len(bits) != 2:
        raise template.TemplateSyntaxError(_('%s tag requires a queryset') % bits[0])

    queryset_var = template.Variable(bits[1])

    template_nodes = parser.parse(('endrecursetree',))
    parser.delete_first_token()

    return RecurseTreeNode(template_nodes, queryset_var)