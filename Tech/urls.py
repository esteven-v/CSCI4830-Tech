from django.urls import path
from .views import front_page
from .views import add_Amiibo
from .views import search_Amiibo
from .views import edit_Amiibo
from .views import delete_Amiibo

urlpatterns = [
    path("", front_page, name="front_page"),
    path("add/", add_Amiibo, name="add_Amiibo"),
    path("search/", search_Amiibo, name="search_Amiibo"),
    path(
        "edit_Amiibo/<int:Amiibo_id>/<int:page_number>/",
        edit_Amiibo,
        name="edit_Amiibo",
    ),
    path(
        "delete_Amiibo/<int:Amiibo_id>/<int:page_number>/",
        delete_Amiibo,
        name="delete_Amiibo",
    ),
]
