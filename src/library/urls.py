from django.urls import path

from library.views import book_detail, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
]
