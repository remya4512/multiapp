from django.urls import path,include
from .import views
urlpatterns = [
    path('app3home',views.app3home,name="app3home"),
    path('details',views.details,name="details"),
    path('register',views.register,name="register"),
]