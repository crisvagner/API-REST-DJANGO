## API REST - DJANGO

### SOBRE O PROJETO

O projeto é uma API Rest desenvolvida com Django e MySQL. Com esta API é possível fazer CRUD tanto de usuários como de posts/notes, e para realizar estas ações é necessário estar autenticado.

- CRUD de posts/notes.
- Endpoints de Cadastro/Login.
- Os administradores podem deletar usuários.
- Os usuários comuns so podem deletar suas proprias contas e seus proprios posts/notes. Terá um mensagem de erro caso tente deletar algo ou atualizar algo que não os pertence.

### OBJETIVO

Aprender sobre o desenvolvimento de APIs com Django.

### INSTRUÇÕES

Para rodar o servidor da API Rest, você tem que criar um banco de dados e passar as configurações dele no arquivo env, após isto, digite os seguintes comandos:

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### OBSERVAÇÕES

Use sempre a "/" no final das rotas. Caso contrário o framework Django retorna um erro.

Para ter as permissões de administrador você precisa logar na página de Admin do Django. Assim você terá acesso a todas as tabelas da aplicação e poderá editar os dados. Crie sua conta de administrador(superusuario) digitando o seguinte comando:

```bash
python manage.py createsuperuser
```

Depois disto, preencha os dados pedidos através do seu terminal.
Agora rode novamente o servidor e cole a seguinte url no seu navegador:

```bash
http://127.0.0.1:8000/admin/login/?next=/admin/
```

O Django não irá redirecionar você para a página onde fica as tabelas. Então aqui está a url da página de tabelas para que você possa manipulá-las com permissões de administrador:

url da página de administrador:

```bash
http://127.0.0.1:8000/admin/
```

### Rotas para Usuário

Rota para registrar usuário:
método POST

request =  (username, email e senha)

```bash
localhost:8000/register/
```

Rota para fazer login:
método POST

request =  (username, email e senha)

```bash
localhost:8000/login/
```

Rota para retornar 1 usuário pelo id:
método GET

```bash
localhost:8000/users/id/
```

Rota para retornar todos os usuários:
método GET

```bash
localhost:8000/users/
```

Rota para atualizar 1 usuário:
método PUT

```bash
localhost:8000/users/id/
```

Rota para deletar 1 usuário:
método DELETE

```bash
localhost:8000/users/id/
```

### Rotas para Posts/Notas

request = (apenas titulo e conteúdo)

Não é preciso informar o id do usuário autor pois o id é passado na requisição automaticamente.
Assim o post/note ficará ligado ao usuário.

Rota para registrar um note:
método POST

```bash
localhost:8000/notes/
```

Rota para retornar 1 note de 1 usuário pelo id:
método GET

```bash
localhost:8000/notes/id/
```

Rota para retornar todos os notes de 1  usuário:
método GET

```bash
localhost:8000/notes/
```

Rota para atualizar 1 note:
método PUT

```bash
localhost:8000/notes/id/
```

Rota para deletar 1 note:
método DELETE

```bash
localhost:8000/notes/id/
```
