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
import json
# import export_csv
from django.core.management.base import BaseCommand
from stellar_base.address import Address
# import stellar_base as sb
from stellar_base.builder import Builder
from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.operation import Payment, ChangeTrust
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope as Te
from stellar_base.memo import TextMemo
from stellar_base.horizon import horizon_testnet, horizon_livenet

def printAccountInfo(publickey):
     #publickey: 'GCZ2MXFXT44Z3OMXF4RZBS4BEWOOQR4EFVSJMNIR3JZ5GTRI7Y2TJLM6'
    address = Address(address=publickey)  # address = Address(address=publickey,network='public') for livenet
    address.get()  # get the updated information

    return address.balances

def getPrimaryKey(key, valu1):
    entry = Question.objects.get(pk =key)
    entry.cardFound = valu1
    entry.save()

def paginated_search_results(request, c):
    print("*"*10)
    accountInfo = printAccountInfo(c[0])
    entry = Question.objects.all()

    for e in entry:
        e.cardFound = 0
        e.save()

    for dict in accountInfo:
        if('asset_code' in dict):
            if(dict['asset_code'] == "SSR" and (float(dict['balance'])) >= 100.0):
                getPrimaryKey(0, 1)
                print("SSR")
            elif(dict['asset_code'] == "CRD" and (float(dict['balance'])) >= 100.0):
                getPrimaryKey(1, 1)
                print("CRD")
            elif(dict['asset_code'] == "USD" and (float(dict['balance'])) >= 100.0):
                getPrimaryKey(2,1)
                print("USD")
            elif(dict['asset_code'] == "CNY" and (float(dict['balance'])) >= 100.0):
                getPrimaryKey(3,1)
                print("USD")

    print("*"*10)
    entry = Question.objects.all()

    # entry.cardFound = 1
    # entry.save()
    # entry = entry.count()
    return render(request, 'saferdb/list.html', { 'contacts': entry})




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
