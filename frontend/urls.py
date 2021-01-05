from django.urls import path
# importamos las class-base views. from django.contrib.auth
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views


app_name = "frontend"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', user_views.register, name='register'),
    # este LoginView necesita un template ya que busca en registratin/login.html por defecto
    # al especificar el template name le asignamos la ruta del nuestro.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
