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


# Fazer no windows ao invés de python app.py-> 
# set FLASK_App=app.py
# flask run