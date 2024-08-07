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

```sh

```
