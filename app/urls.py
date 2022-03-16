from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path("profile/", views.my_profile, name="profile"),
    path('accounts/profile/', views.home, name="home"),
    path('upload/', views.uploadProject, name='add_project'),
    re_path(r'^api/profile/$', views.ProfileList.as_view()),
    re_path(r'^api/project/$', views.ProjectList.as_view()),
    path("project/<int:project_id>/", views.vote_details, name="vote_details"),
    path("project/rate/<int:id>/", views.rate, name="rate"),
    path("search/", views.search, name="search"),
    path('logout/', views.logoutUser, name='logoutii'),

]