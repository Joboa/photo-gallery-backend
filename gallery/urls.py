from django.urls import path
from .views import ListImage, DetailImage


urlpatterns = [
    path('<int:pk>/', DetailImage.as_view()),
    path('', ListImage.as_view()),
]
 