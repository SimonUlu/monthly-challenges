from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)
        

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
       challenge_text = "January"
    elif month == "february":
        challenge_text = "February"
    else:
        return HttpResponseNotFound("Month is not supported")
        
    return HttpResponse(challenge_text)