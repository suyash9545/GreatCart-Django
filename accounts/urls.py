from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("", views.dashboard, name='dashboard'),
    path("forgotPassword/", views.forget_password, name='forgotPassword'),
    path("reset_password_validate/<uidb64>/<token>", views.reset_password_validate, name='reset_password_validate'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset_password/', views.reset_password, name='reset_password')

]
