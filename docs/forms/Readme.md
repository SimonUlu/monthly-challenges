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

## Adding form data to db

- add this stuff to view (in template just call form) the names of the columns have to match from db to form

```sh
def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        ## or updating an existing data
        ##form = ReviewForm(request.POST, instance=Review.objects.get(pk=1))
        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data["user_name"],
                review_text=form.cleaned_data["review_text"],
                rating= form.cleaned_data["rating"],
            )
            review.save()
            ## or: (only if you work with ModelForms)
            ## form.save() 
            return redirect("thank_you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})
```


## Model forms


```sh
from .models import Review

## instead of doing this

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name",max_length=255, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name",
    })
    review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=255)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

## just add this

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        ##either one of the following
        fields = '__all__'
        #exclude = ["owner"]
        #fields = ["user_name", "rating"]
        
```

## Configuring the modelform

```sh
## configure your meta for example as follows
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        #exclude = ["owner"]
        #fields = ["user_name", "rating"]
        labels = {
            "user_name": "Your Name",
            "review_text": "Your review text",
            "rating": "Your rating"
        }
        error_messages = {
            "user_name": {
              "required": "Your name must be required" ,
              "max_length": "You have to set a max length",
            },
            "review_text": "Your review text",
            "rating": "Your rating"
        }
```

## Class based views instead of functions

-- but for example smth like this in views.py:

```sh
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
``` 

- change url ins urls.py like follows:

```sh
    path('', views.ReviewView.as_view()),  
```
