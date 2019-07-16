from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('pod/viewer.html')

    context = {}
    render_index = template.render(context, request)

    return HttpResponse(render_index)
