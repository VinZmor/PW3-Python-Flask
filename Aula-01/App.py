# Importando o Flask
from flask import Flask

# Carregando o Flask na variável app
app = Flask(__name__)

# Criando a primeira rota do site. 
    # Rota com uma '/' é a rota principal
@app.route('/')

# Criando função Python
def home():
        return '<h1> Bem-Vindo ao meu primeiro site em Flask </h1>'

if __name__ == '__main__': #Rodar caso for o principal. Quando o código está na frente do If, ele considera, caso contrario ele não considera

    # Inicia o servidor, porta 5000, como modo de depuração ativado
    app.run (host='localhost', port=5000, debug=True)
