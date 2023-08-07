from django.urls import path
from . import views

urlpatterns = [
    path('first_app/',views.first_app , name = 'first_app' )
]