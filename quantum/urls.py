
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('signup/login', views.login, name='login'),
    path('signup/login/pdf_stock', views.pdf_stock, name='pdf_stock'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    ]
