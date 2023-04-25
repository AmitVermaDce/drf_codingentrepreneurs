from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.products_alt_view),
    path("", views.products_alt_view),
] 
