from django import template
import ast
register = template.Library()


@register.filter
def stringtodict(value):
    try:
        print(ast.literal_eval(value))
        
        return ast.literal_eval(value).items()
    except Exception as e:
        print(e)
        return dict()