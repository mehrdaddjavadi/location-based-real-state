from .views import ListingListView
from django.urls import path

urlpatterns = [
    path('listings/',ListingListView.as_view()),
]
