from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.get_tasks),
    path("tasks/stats/", views.productivity_stats)
]
