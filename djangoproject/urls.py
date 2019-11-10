from django.contrib import admin
from django.urls import path,include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    UserFilter,


)
from django_filters.views import FilterView

from . import views

urlpatterns = [

    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),

    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('news/',PostListView.as_view(),name='news'),
    path('about/',views.about,name='blog-about'),
    path('team/',views.Team,name='team'),
    path('test_skills',views.Skills,name='test_skills'),
    path(r'search/',FilterView.as_view(filterset_class=UserFilter,template_name='djangoproject/search_box.html'),name='search-blog'),
    path(r'search_review/',FilterView.as_view(filterset_class=UserFilter,template_name='djangoproject/search_box_2.html'),name='search-blog-review'),
    path(r'ask_question/',views.askquestion,name='ask-question'),
    path(r'view_question/<int:qid>/<slug:qslug>', views.viewquestion,name='view-question'),
    path(r"^comments/", include("pinax.comments.urls", namespace="pinax_comments")),
    



    ]

