"""from django.urls import path
from . import views

urlpatterns = [
  path('', views.birthday, name="birthday"),
    
]"""

from django.urls import path
from django.views.generic import RedirectView
from birthday.views import birthday_message

urlpatterns = [
    path("", birthday_message, name="birthday"),
]
