from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'home.htm')


def count(req):
    return render(req, 'count.htm')
