## Create post form with file upload and return

html:

```sh

  <form action="/profiles/" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="image" id="image" />
    <button>Upload!</button>
  </form>

```

```sh
class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        files = request.FILES["image"]
        print(files)
        
        return redirect("/profiles")
```


## use django helper functions to simplify file upload


- add the following to the settings.py of the base projects folder

```sh
MEDIA_ROOT = BASE_DIR / "uploads"
```

- models

```sh
class UserProfile(models.Model):
    image = models.FileField(
        upload_to="images"
    )  ## it will take the file and store it to hard-drive and only the path to the db
```

-views

```sh
    def post(self, request):
        
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return redirect("/profiles")
        
        
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })
```


## serving uploaded files

- serving uploaded files

add this to settings.py of project
```sh
MEDIA_URL = "/user-media/"
```

add this to urls.py of main project

```sh
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include("challenges.urls")),
    path('reviews/', include("reviews.urls")),
    path('profiles/', include("profiles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```