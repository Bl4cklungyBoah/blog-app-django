from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register, frontpage

urlpatterns = [
    path('frontpage/', frontpage, name='frontpage'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='frontpage'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
]