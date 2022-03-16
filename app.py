from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)



# O decorator aplicando o método 'route' passando ('/) em cima da função 'index'.
# app.route -> cria a rota da página
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


# Só vai dar o run se esse (app.py no caso) for o arquivo principal da aplicação
if __name__ == 'main':
    app.run()


"""
# Aula 3 - Resumo para criação do ambiente
>> -----------------------------------<<
01. 
"""