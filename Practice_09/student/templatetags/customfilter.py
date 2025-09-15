from django import template
register = template.Library()

# Without Decorator
# def myreplace(value, arg):
#     return value.replace(arg, 'Backend Developer')

# register.filter('DeveloperToBackenddeveloper', myreplace)

# With Decorator
@register.filter(name='DeveloperToBackenddeveloper')
def myreplace(value, arg):
    return value.replace(arg, 'Backend Developer')

