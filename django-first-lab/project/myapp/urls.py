from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("demo", views.index, name="index"),
    path("main", views.main, name="main"),
    path("header", views.header, name="header"),
    path("getuser/<name>/<id>", views.pathview, name="pathview"),
    path("getuser/", views.qryview, name="qryview"),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name="getform"),
    path("dishes/<str:dish>", views.menuitems),
    path("menu/", views.menu, name="menu"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("home/", views.form_view),
]
