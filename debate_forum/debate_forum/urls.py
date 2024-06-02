from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.debate_list, name='debate_list'),
    path('<int:pk>/', views.debate_detail, name='debate_detail'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_debate, name='create_debate'),
    path('<int:pk>/post/', views.create_post, name='create_post'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
