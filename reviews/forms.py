from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name",max_length=255, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name",
    })
    