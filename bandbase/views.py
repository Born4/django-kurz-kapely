from django.shortcuts import render
from django.http import HttpResponse


def home_page(request, *args, **kwargs):
    """Jednoducha dekovaci stranka po odeslani formulare

    DATA NOT OK
    """
    return HttpResponse('<h2>Domovska stranka projektu...</h2>')


def data_odeslana_data_ok(request, *args, **kwargs):
    """Jednoducha dekovaci stranka po odeslani formulare

    DATA OK
    """
    return HttpResponse('Data ok...')


def data_odeslana_bad_data(request, *args, **kwargs):
    """Jednoducha dekovaci stranka po odeslani formulare

    DATA NOT OK
    """
    return HttpResponse('Bad data !!!')


