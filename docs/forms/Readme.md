## Create a file forms.py in app-folder

- this can be used in template

```sh
from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=255)
    
```

## Register new view/route for forms with Post and get

```sh
def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("thank_you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")

```

- in the template form can be used by simply adding {{form}}

## Customizing form controls

for example

```sh
class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name",max_length=255, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name",
    })
    review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=255)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
```

visit docs for further customization: https://docs.djangoproject.com/en/5.0/ref/forms/fields/