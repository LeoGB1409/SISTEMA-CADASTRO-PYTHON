# PT-BR
# Sistema de Cadastro de Usuários

Aplicação web desenvolvida com Django para cadastrar usuários e listar os registros armazenados em um banco SQLite.

## Funcionalidades

- Cadastro de usuários com nome e idade
- Listagem dos usuários cadastrados
- Navegação entre a página de cadastro e a lista
- Interface baseada em templates Django e Bootstrap

## Tecnologias

- Python
- Django
- SQLite
- HTML
- Bootstrap 5

## Estrutura do projeto

```text
SISTEMA-CADASTRO/
|-- .venv/
`-- projeto_cad_users/
    |-- app_cad_users/
    |   |-- migrations/
    |   |-- templates/usuarios/
    |   |-- models.py
    |   |-- views.py
    |   `-- urls.py
    |-- projeto_cad_users/
    |   |-- settings.py
    |   `-- urls.py
    |-- db.sqlite3
    `-- manage.py
```

## Modelo de dados

A aplicação utiliza o modelo `usuarios` com os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `id_usuario` | `AutoField` | Identificador gerado automaticamente |
| `nome` | `CharField` | Nome do usuário |
| `idade` | `IntegerField` | Idade do usuário |

## Como executar

### 1. Acesse a pasta do projeto

```powershell
cd PYTHON\SISTEMA-CADASTRO
```

### 2. Crie e ative o ambiente virtual

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação, use:

```powershell
.venv\Scripts\activate.bat
```

### 3. Instale o Django

```powershell
python -m pip install django
```

### 4. Prepare o banco de dados

```powershell
cd projeto_cad_users
python manage.py migrate
```

### 5. Inicie o servidor

```powershell
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador.

## Rotas

| Rota | Descrição |
|---|---|
| `/` | Formulário de cadastro |
| `/usuarios/` | Lista de usuários cadastrados |

## Observações

- O projeto já contém o arquivo `db.sqlite3`.
- As migrações são armazenadas em `app_cad_users/migrations`.
- Este projeto utiliza a configuração padrão de desenvolvimento do Django e não deve ser exposto diretamente em produção sem ajustes de segurança.

# EN
# User Registration System

A web application developed with Django to register users and list the records stored in an SQLite database.

## Features

- User registration with name and age
- List of registered users
- Navigation between the registration page and the list
- Interface based on Django templates and Bootstrap

## Technologies

- Python
- Django
- SQLite
- HTML
- Bootstrap 5

## Project Structure

```text
SISTEMA-CADASTRO/
|-- .venv/
`-- projeto_cad_users/
    |-- app_cad_users/

    |   |-- migrations/
    |   |-- templates/usuarios/
    |   |-- models.py
    |   |-- views.py
    |   `-- urls.py
    |-- projeto_cad_users/

    |   |-- settings.py
    |   `-- urls.py
    |-- db.sqlite3
    `-- manage.py
```

## Data Model

The application uses the `usuarios` model with the following fields:

| Field | Type | Description |
|---|---|---|
| `id_usuario` | `AutoField` | Automatically generated identifier |
| `nome` | `CharField` | User's name |
| `idade` | `IntegerField` | User's age |

## How to Run

### 1. Access the project folder

```powershell
cd PYTHON\SISTEMA-CADASTRO
```

### 2. Create and activate the virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks execution, use:

```powershell
.venv\Scripts\activate.bat
```

### 3. Install Django

```powershell
python -m pip install django
```

### 4. Prepare the database

```powershell
cd projeto_cad_users
python manage.py migrate
```

### 5. Start the server

```powershell
python manage.py runserver
```

Access `http://127.0.0.1:8000/` in your browser.

## Routes

| Route | Description |
|---|---|
| `/` | Registration form |
| `/usuarios/` | List of registered users |

## Notes

- The project already contains the `db.sqlite3` file.
- Migrations are stored in `app_cad_users/migrations`.
- This project uses Django's default development configuration and should not be directly exposed to production without security adjustments.
