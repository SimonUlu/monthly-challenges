## Register different sub-apps in main project folder

```sh
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenge/', include("challenges.urls"))
]
```

## Register different urls in subapp that correspond to subpath

- when configuring single url to be equiv to int and str link always use int first (otherwise it won't work)
- name is equal to route namespaces in laravel
- views. is the function that you define in views.py

```sh
from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
```

## Return Http Response for view function

- try to infuse try/catch blocks for error handling

```sh
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]   
    except:
        return HttpResponseNotFound("Monat nicht gefunden")
    
    return HttpResponse(challenge_text)
```

## Http Response not found for returning 404 page or error message to user

```sh
return HttpResponseNotFound("Monat nicht gefunden")
```

## Return reverse function to equal url schema

```sh
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
```

```sh
from django.urls import reverse

redirect_path = reverse("month-challenge", args=[redirect_month])

return HttpResponseRedirect(redirect_path)
```


## Return html instead of only strings

- via html string interpolation

```sh
response_data = f"<h1> {challenge_text} </h1>" 

return HttpResponse(response_data)
```


