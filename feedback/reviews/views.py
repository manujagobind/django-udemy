from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def review(request):
    if request.method == 'POST':
        return HttpResponseRedirect("/thank-you")
    return render(request, 'reviews/review.html')

def thank_you(request):
    return render(request, 'reviews/thank-you.html')