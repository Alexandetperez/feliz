"""from django.urls import path
from . import views

urlpatterns = [
  path('', views.birthday, name="birthday"),
    
]"""

from django.urls import path
from django.views.generic import RedirectView
from birthday.views import brithday

urlpatterns = [
    path(
        "", RedirectView.as_view(url="/birthday/")
    ),  # Redirecciona la URL base a la URL deseada
    path("birthday/", brithday, name="birthday"),
]
