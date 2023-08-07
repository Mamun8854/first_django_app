from django.contrib import admin
from django.urls import path,include
from first_app.views import *
urlpatterns = [
    path('', first_app , name="first_app"),
    path("success-page/", success_page ,name="success_page"),
    path('admin/', admin.site.urls),
]
