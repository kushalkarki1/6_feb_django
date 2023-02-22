from django.urls import path
from post.views import home, create_post, edit_post, delete_post

app_name="post"

urlpatterns = [
    path("", home, name="home"),
    path("create-post/", create_post, name="create_post"),
    path("edit-post/<int:postid>/", edit_post, name="edit_post"),
    path("delete-post/", delete_post, name="delete_post"),
]