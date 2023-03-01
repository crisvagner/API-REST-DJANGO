from Users.api.viewsets import UsersViewSet, CreateUserView
from Notes.api.viewsets import NotesViewSet

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
