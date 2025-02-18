# Importando o Flask e o render_templante (que lê o html)
from flask import Flask, render_template

# Carregando o Flask na variável app. template_folder localiza a página
app = Flask(__name__, template_folder='views')

# Criando a primeira rota do site. 
    # Rota com uma '/' é a rota principal
@app.route('/')

# Criando função Python
def home():
    return render_template('index.html')

# Assim cria outras rotas. Deve adicionar o /nome no link da página
@app.route('/games')


def game():
    titulo = 'CS:GO'
    ano = 2012
    categoria = 'FPS Online'
    # Array funciona assim:
    jogadores = ['Vinícius', 'Zezília', 'Moreira', 'Pereira']
    jogos = ['The Sim 4', 'Lethal Comphany', 'Stardey Valley', 'FIFA 17', 'Pokemon Fire Red', 'GTA 5']
    
    return render_template('games.html', 
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores,
                           jogos=jogos)



if __name__ == '__main__': #Rodar caso for o principal. Quando o código está na frente do If, ele considera, caso contrario ele não considera

    # Inicia o servidor, porta 5000, como modo de depuração ativado
    app.run (host='localhost', port=5000, debug=True)
