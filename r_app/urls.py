from django.contrib import admin
from django.urls import path
from r_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
]
