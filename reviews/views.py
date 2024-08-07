from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class ReviewView(View):
    def get(self, request):

        form = ReviewForm()

        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
        
        return render(request, "reviews/review.html", {"form": form})


def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


    

class ThankYouView(TemplateView):
    
    template_name = "reviews/thank_you.html"
    
