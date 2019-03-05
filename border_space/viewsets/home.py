from django.template import Template, RequestContext
from django.http import HttpResponse

def home(request):
    fp = open('border_space/templates/home.html')
    html = Template(fp.read())
    fp.close()
    context = RequestContext(request)
    return HttpResponse(html.render(context))