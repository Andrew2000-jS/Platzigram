from django.urls import path
from posts import views

urlpatterns = [
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='posts/feed',
        view=views.PostFeedView.as_view(),
        name="feed"
    ),
    path(
        route='posts/new',
        view=views.CreatePostView.as_view(),
        name="create"
    ),
]
