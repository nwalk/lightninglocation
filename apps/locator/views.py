##from django.shortcuts import render
from django.views import generic


class MainView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'locator/main.html'


class MapView(generic.TemplateView):
    """Loads the map page"""
    template_name = 'locator/map.html'