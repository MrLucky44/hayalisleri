from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class FlightsView(TemplateView):
    template_name = "flights/flights.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = range(6)
        return context
