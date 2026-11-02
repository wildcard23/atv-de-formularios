# Cadastro de autores

Aplicação Django para listar livros e cadastrar autores sem usar o admin. O formulário é um `ModelForm`; o nome é obrigatório e a nacionalidade é opcional. Para executar localmente:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

A lista de livros fica em `/livros/`. O link **Novo autor** abre `/autores/novo/`. Após o envio válido, a aplicação redireciona para a página do autor, evitando que atualizar a página repita o POST e crie outro registro.

## Proteção CSRF

O formulário inclui `{% csrf_token %}` e o middleware `CsrfViewMiddleware` está ativo. Se a tag for removida do template, o navegador envia o POST sem o token exigido e o Django responde com **403 Forbidden**; o autor não é salvo. O teste `test_missing_csrf_token_is_rejected` verifica esse comportamento com as verificações CSRF habilitadas no cliente de teste.

Execute os testes com `python manage.py test`.