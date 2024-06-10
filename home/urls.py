from django.urls import path
from .views import *

urlpatterns = [
    path("student/", StudentAPI.as_view()),
# path("",home, name="home"),
# path("student/",post_student, name="student"),
# path("delete/<int:id>/",delete_student, name="update_Student"),
path("get_book/",get_book)
]