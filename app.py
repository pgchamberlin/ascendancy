#!python

# import and intialize Flask
from flask import Flask, Response
app = Flask(__name__)

# import and initialize Ascendancy
from ascendancy.core import Ascendancy
ascendancy = Ascendancy()

@app.route('/')
def index():
    response_body, keyed_args_dict = ascendancy.index()
    return Response(response_body, **keyed_args_dict)

@app.route('/players', methods = ['GET'])
def get_players():
    response_body, keyed_args_dict = ascendancy.get_players()
    return Response(response_body, **keyed_args_dict)

@app.route('/players', methods = ['POST'])
def new_player():
    response_body, keyed_args_dict = ascendancy.new_player(request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/players/<id>', methods = ['GET'])
def get_player(id):
    response_body, keyed_args_dict = ascendancy.get_player(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/players/<id>', methods = ['PUT'])
def update_player(id):
    response_body, keyed_args_dict = ascendancy.update_player(id, request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/players/<id>', methods = ['DELETE'])
def delete_player(id):
    response_body, keyed_args_dict = ascendancy.delete_player(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/games', methods = ['GET'])
def get_games():
    response_body, keyed_args_dict = ascendancy.get_games()
    return Response(response_body, **keyed_args_dict)

@app.route('/games', methods = ['POST'])
def new_game():
    response_body, keyed_args_dict = ascendancy.new_games(request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/games/<id>', methods = ['GET'])
def get_game(id):
    response_body, keyed_args_dict = ascendancy.get_game(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/games/<id>', methods = ['PUT'])
def update_game(id):
    response_body, keyed_args_dict = ascendancy.update_game(id, request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/games/<id>', methods = ['DELETE'])
def delete_game(id):
    response_body, keyed_args_dict = ascendancy.delete_game(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitions', methods = ['GET'])
def get_competitions():
    response_body, keyed_args_dict = ascendancy.get_competitions()
    return Response(response_body, **keyed_args_dict)

@app.route('/competitions', methods = ['POST'])
def new_competition():
    response_body, keyed_args_dict = ascendancy.new_competition(request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitions/<id>', methods = ['GET'])
def get_competition(id):
    response_body, keyed_args_dict = ascendancy.get_competition(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitions/<id>', methods = ['PUT'])
def update_competition(id):
    response_body, keyed_args_dict = ascendancy.update_competition(id, request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitions/<id>', methods = ['DELETE'])
def delete_competition(id):
    response_body, keyed_args_dict = ascendancy.delete_competition(id)
    return Response(response_body, **keyed_args_dict)

if __name__ == '__main__':
    app.run(debug=True)

