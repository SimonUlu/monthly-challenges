from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "user_name": "Your Name",
            "review_text": "Your review text",
            "rating": "Your rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name",
            },
            "review_text": {
                "required": "Your review must not be empty",
            },
            "rating": {
                "required": "Please provide a rating",
                "min_value": "The rating must be at least 1",
                "max_value": "The rating must be at most 5",
            }
        }
