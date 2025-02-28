from flask import render_template, request

jogadores = ['Vinícius', 'Zezília', 'Moreira', 'Pereira']


def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():

        game = {"titulo": 'CS:GO',
                "ano": 2012,
                "categoria": 'FPS Online', }

        jogos = ['The Sim 4', 'Lethal Comphany', 'Stardey Valley',
                 'FIFA 17', 'Pokemon Fire Red', 'GTA 5']

        # Tratado se a requisição for do tipo post
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))

        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               )
