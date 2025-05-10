from django.urls import path

from . import views
from django.conf.urls.static import static
app_name = "game"
urlpatterns = [
    path("play/", views.index, name="index"),
    path("", views.login, name="login"),
]