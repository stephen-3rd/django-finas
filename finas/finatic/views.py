from django.shortcuts import render
from django.views import generic
from .models import Lust

# Create your views here.


class LustView(generic.ListView):
    queryset = Lust.objects.filter(status=1).order_by('-date')
    template_name = 'finatic/lust_page.html'


class LustDetail(generic.DetailView):
    model = Lust
    template_name = 'finatic/lust_detail.html'

