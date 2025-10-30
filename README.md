# Django

A Django starter template as per the docs: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

## Como executar localmente (Windows)

1. Crie e ative um virtualenv (se ainda não existir):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instale dependências:

```powershell
python -m pip install -r mysite/requirements.txt
```

3. Variáveis de ambiente úteis (desenvolvimento):

- `DJANGO_SECRET_KEY` — chave secreta (opcional; há fallback para desenvolvimento)
- `DJANGO_DEBUG` — `True` ou `False` (padrão: `True`)

Exemplo no PowerShell:

```powershell
$env:DJANGO_DEBUG = 'True'
$env:DJANGO_SECRET_KEY = 'minha_chave_secreta_local'
```

4. Executar migrações e criar superuser:

```powershell
python mysite/manage.py migrate
python mysite/manage.py createsuperuser
```

5. Rodar a aplicação localmente:

```powershell
python mysite/manage.py runserver
```

6. Rodar testes:

```powershell
python mysite/manage.py test core -v 2
```

Observação: Evite comitar `SECRET_KEY` em repositórios públicos; use variáveis de ambiente ou um vault para produção.
