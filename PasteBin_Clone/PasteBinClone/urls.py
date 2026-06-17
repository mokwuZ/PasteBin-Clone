from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),
    path("resultList", views.resultList, name="resultList"),
    path("detailedResult/<int:userNum>", views.detailedResult, name="detailedResult"),
]