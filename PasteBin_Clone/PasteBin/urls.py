from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),
    path("usersList", views.usersList, name="usersList"),
    path("usersDetails/<int:userNum>", views.usersDetails, name="usersDetails"),
    path("usersDetails/savedDataUsers", views.savedDataUsers, name="savedDataUsers"),
]