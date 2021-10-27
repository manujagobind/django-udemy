from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "max_length": "Please enter a shorter name",
        "required": "Your name must not be empty"
    })
    review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)