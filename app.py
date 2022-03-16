from flask import Flask

app = Flask(__name__)

# O decorator aplicando o método 'route' passando ('/) em cima da função 'index'.
# app.route -> cria a rota da página
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


# Só vai dar o run se esse (app.py no caso) for o arquivo principal da aplicação
if __name__ == 'main':
    app.run()


"""
# Aula 2 - Resumo para criação do ambiente
>> -----------------------------------<<
01. python -m venv env
02. pip install virtualenv
03. virtualenv env
04. source env/Scripts/activate
05. set FLASK_APP = app.py
06. flask run
"""