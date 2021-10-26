from django.urls import path

from .views import review, thank_you

urlpatterns = [
    path("", review),
    path('thank-you', thank_you)
]
