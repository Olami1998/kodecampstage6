from pathlib import Path
from django.urls import path
from .views import Signup, login_view, logout_view, home, add_customer

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("manage-signup/", Signup, name="manage_signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"), 
    path("add_customer/", add_customer, name="add_customer"),
    #path("fetch-book/", fetch_book, name="fetch_book"),
    #path("update-book/", update_book, name="update_book"),
    #path("updating/", updating, name="updating"),
    #path("delete/", delete_view, name="delete"),
    #path("deleting/", deleting, name="deleting"),
]