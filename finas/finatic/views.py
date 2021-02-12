from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Lust

# Create your views here.


class LustView(generic.ListView):
    queryset = Lust.objects.filter(status=1).order_by('-time')
    context_object_name = 'lust_page'
    template_name = 'finatic/lust_page.html'


class LustDetail(generic.DetailView):
    model = Lust
    context_object_name = 'lust_detail'
    template_name = 'finatic/lust_detail.html'


class CreateLustr(CreateView):
    model = Lust
    fiels = ['title', 'picture', 'description', 'slug', 'status']

