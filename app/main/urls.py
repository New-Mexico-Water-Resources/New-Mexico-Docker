from django.urls import path

from . import views
# from .views import water_rights

urlpatterns = [
    path("", views.home, name="home"),
    path("view/", views.view, name="index"),
    path("home/", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
    path("water_rights_upload/", views.water_rights_upload, name="water_rights_upload"),
    path("water_rights_processing/", views.water_rights_processing, name="water_rights_processing"),
    path("water_rights_status/", views.water_rights_status, name="water_rights_status")
]
