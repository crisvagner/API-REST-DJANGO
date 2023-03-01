from Users.api.viewsets import UsersViewSet, CreateUserView
from Notes.api.viewsets import NotesViewSet

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Importa o pacote routers do Django REST Framework
from rest_framework import routers

# Cria um objeto router do tipo DefaultRouter do Django REST Framework
router = routers.DefaultRouter()

# Registra as rotas para os ViewSets UsersViewSet e NotesViewSet no router
router.register(r'users', UsersViewSet, basename='Users')
router.register(r'notes', NotesViewSet, basename='Notes')

# Define as rotas da aplicação
urlpatterns = [
    # Rota para a página de administração do Django
    path('admin/', admin.site.urls),
    # Inclui as rotas definidas no router
    path('', include(router.urls)),
    # Rota para a página de login da aplicação
    path('login/', include('Users.urls')),
    # Rota para a página de registro de usuários da aplicação
    path('register/', CreateUserView.as_view()),
]
