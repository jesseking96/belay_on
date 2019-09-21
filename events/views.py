from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.
class EventListView(generic.list.ListView):
    model = models.Event

    template_name = 'events/event_list_view.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.object_list
        return context

class EventDetailView(generic.detail.DetailView):
    model = models.Event
    template_name = 'events/event_detail_view.html'
