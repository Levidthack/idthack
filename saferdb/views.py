from django import forms
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from saferdb.forms import HomeForm, QueryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.forms.models import model_to_dict
from django.views import generic
from django.views.generic import TemplateView
from .models import Question, Query
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import  logging
import csv
# import export_csv
from django.core.management.base import BaseCommand



def paginated_search_results(request, c):

    entry = Question.objects.get(pk =c[0])

    entry.cardFound = 1
    entry.save()
    count = 'stuff'
    entry = Question.objects.all()
    # entry = entry.count()
    return render(request, 'saferdb/list.html', {'contacts': entry})



@method_decorator(login_required, name='post')
class QueryView(ListView):
    template_name= 'saferdb/query.html'
    global d

    def get(self, request):
        global d
        if request.GET.get('page'):
            return paginated_search_results(request, d)
        form = QueryForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        global d
        d = None
        d = request.POST.getlist('opeclass')
        return paginated_search_results(request, d)


################################################################################
class HomeView(TemplateView):

    template_name = 'saferdb/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = HomeForm (request.POST)
        c = request.POST.getlist('vehicle')
        if c[0] == 'Bike':
            args ={'form': form, 'text': 'success'}
            return render(request, 'saferdb/search.html', args )

        if form.is_valid():
            text = form.cleaned_data['post']
        else:
            return HttpResponse("Youre entry was invalid.")
        args ={'form': form, 'text': 'stuff'}
        return render(request, 'saferdb/search.html', args )
