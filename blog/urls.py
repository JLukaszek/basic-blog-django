from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(),
         name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(),
         name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='post_delete'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
