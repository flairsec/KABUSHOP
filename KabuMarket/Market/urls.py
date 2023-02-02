from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('product/<str:pk>',views.product, name='product')
]


