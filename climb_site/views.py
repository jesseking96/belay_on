from django.shortcuts import render
from django.views import generic
# Create your views here.
class Index(generic.base.TemplateView):
    template_name = "climb_site/index.html"

    def get_context_data(self):
        pass

class About(generic.base.TemplateView):
    template_name = "climb_site/about.html"

    def get_context_data(self):
        pass
