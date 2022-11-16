from django.shortcuts import render
from django.views.generic import ListView
from .models import Pessoa


class ListPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all.order_by('nome_compelto')
