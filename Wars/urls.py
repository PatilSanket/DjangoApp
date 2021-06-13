from django.urls import path
from . import views

urlpatterns = [
   path("", views.AllBattles),
   path("<ID>", views.Battle_by_ID),
   path("Aggr",views.Aggregates)
]