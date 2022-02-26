from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path("", views.hello_word, name = "home")
]
