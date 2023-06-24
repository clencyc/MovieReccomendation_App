from django.shortcuts import render

from django.http import HttpResponse

def wani(request):
    return HttpResponse("Hello From Recommender!")