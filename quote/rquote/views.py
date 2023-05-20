from django.shortcuts import render
from django.http import JsonResponse
from .models import Quote
from random import randint
from django.http import HttpResponse 
# Create your views here.
def random_quote(request):
    count = Quote.objects.count()
    random_index = randint(0, count - 1)
    quote = Quote.objects.all()[random_index]
    data = {
        'quote': quote.text,
        'author': quote.author
    }
    return JsonResponse(data)

def index(request):

    return HttpResponse("Hello")
