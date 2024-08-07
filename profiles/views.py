from django.shortcuts import render, redirect
from django.views import View

from .forms import ProfileForm

# Create your views here.


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            files = request.FILES["image"]
        
            store_file(files)
            
            return redirect("/profiles")
        
        
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })



        