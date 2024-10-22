# Extrator de Placas para Retroalimentação
## Carregando ambiente virtual

Criando o ambiente virtual:

``` python
virtualenv extrator-placas
```

Ativando o ambiente virtual:

``` python
source extrator-placas/bin/activate
```

Desativando o ambiente virtual:

``` python
deactivate
```

## Instalando as bibliotecas

``` python
pip install -r requirements.txt
```

## Congelando as versões da biblioteca

``` python
pip freeze > requirements.txt
```