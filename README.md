# IGS Internation Solutions

## Este projeto foi feito com:

* [Python 3.8.6](https://www.python.org/)
* [Django 4.0.3](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/marcelovieiratecnologia/mvtec.git
cd mvtec
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```
## Acessar o admin!
http://127.0.0.1:8000/admin
login: admin
password: admin

## Acessar o home:
http://127.0.0.1:8000/

## Acessar o rest para CRUD
http://127.0.0.1:8000/employees/
