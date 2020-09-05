from django.shortcuts import render
from django.template import loader
from cars.models import Car
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q 


class SearchResultsView(ListView):
    model = Car
    template_name = 'index.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Car.objects.filter(
                Q(producer__icontains=query) | Q(model__icontains=query) |
                Q(prod_year__icontains=query) | Q(color__icontains=query)
            )
            return object_list
        else:
            object_list = Car.objects.all()
            return object_list


