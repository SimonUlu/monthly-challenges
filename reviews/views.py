from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    if request.method == "POST":
        entered_username = request.POST["username"]

        if entered_username == "":
            return render(request, "reviews/review.html", {"has_error": True})

        return redirect("thank_you")
    return render(request, "reviews/review.html", {"has_error": True})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
