from django.shortcuts import render, redirect

from .forms import ReviewForm


# Create your views here.


def index(request):
    form = ReviewForm()
    
    return render(request, "reviews/review.html", {
        "form": form
    })
    


def thank_you(request):
    return render(request, "reviews/thank_you.html")
