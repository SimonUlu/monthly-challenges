from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        files = request.FILES["image"]
        
        store_file(files)
        
        return redirect("/profiles")



        