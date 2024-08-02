from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("This is the challenge for february")

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
       challenge_text = "January"
    elif month == "february":
        challenge_text = "February"
    else:
        return HttpResponseNotFound("Month is not supported")
        
    return HttpResponse(challenge_text)