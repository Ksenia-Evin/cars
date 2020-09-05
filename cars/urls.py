from django.urls import path
from .views import SearchResultsView
 
urlpatterns = [
    path('index/', SearchResultsView.as_view(), name='index'),
]