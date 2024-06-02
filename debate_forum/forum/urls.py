from django.urls import path
from . import views

urlpatterns = [
    path('', views.debate_list, name='debate_list'),
    path('<int:pk>/', views.debate_detail, name='debate_detail'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_debate, name='create_debate'),
    path('<int:pk>/post/', views.create_post, name='create_post'),
]
