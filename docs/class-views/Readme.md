## Use view classes instead of function

```sh
class ThankYouView(View):
    
    def get(self, request):
        return render(request, "reviews/thank_you.html")
```

## Template View Class

```sh
class ThankYouView(TemplateView):
    
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["message"] = "This works!"
    return context
```

## check docs for more views