from django.contrib.auth.models import User
from rest_framework import serializers
import bcrypt


# Cria uma classe UsersSerializer que herda da classe ModelSerializer do Django REST Framework
class UsersSerializer(serializers.ModelSerializer):
    # Define a classe Meta para indicar o modelo e campos a serem serializados
    class Meta:
        model = User
        # Define os campos que serão incluídos na serialização
        fields = ['id', 'username', 'email', 'password']

    # Define o método create para criar um novo usuário com uma senha criptografada
    def create(self, validated_data):
        # Obtém a senha do dicionário validated_data e remove-a do dicionário
        password = validated_data.pop('password')
        # Cria uma senha criptografada usando o pacote bcrypt
        hashed_password = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        # Cria um novo usuário com a senha criptografada e os outros dados do dicionário validated_data
        user = User.objects.create(password=hashed_password, **validated_data)
        # Retorna o novo usuário
        return user
