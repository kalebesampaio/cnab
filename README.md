# CNAB
O projeto é um banco onde é armazenado as transações e informações do cliente por meio da CNAB.
Stacks: Python, Django, HTML5, CSS3, JavaScript
## É necessário ter python 3.11.1 ou maior, não foi testado em versões inferiores
## Use os seguintes comandos no seu terminal para rodar a aplicação
### Clone o repositório primeiro
```
git clone git@github.com:kalebesampaio/cnab.git
```
### Crie um ambiente virtual
```
python -m venv venv
```
### Ative o ambiente virtual
No Windows
```
.\venv\Scripts\activate
```
No Linux
```
source venv/bin/activate
```
### Instale as dependências 
```
pip install -r requirements.txt
```
## Rodar migrations e servidor
```
python manage.py migrate
python manage.py runserver
```

## Repositório: https://github.com/kalebesampaio/cnab
