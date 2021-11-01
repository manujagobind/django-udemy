from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {
        "form": form
    })

def thank_you(request):
    return render(request, 'reviews/thank-you.html')