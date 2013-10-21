#!python

# import and intialize Flask
from flask import Flask, Response
app = Flask(__name__)

# import and initialize Sommelier
from ascendancy.core import Ascendancy
ascendancy = Ascendancy()

@app.route('/')
def index():
    response_body, keyed_args_dict = ascendancy.index()
    return Response(response_body, **keyed_args_dict)

@app.route('/ladders', methods = ['GET'])
def get_ladders():
    response_body, keyed_args_dict = ascendancy.get_ladders()
    return Response(response_body, **keyed_args_dict)

@app.route('/ladders', methods = ['POST'])
def new_ladder():
    response_body, keyed_args_dict = ascendancy.new_ladder(request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/ladders/<id>', methods = ['GET'])
def get_ladder(id):
    response_body, keyed_args_dict = ascendancy.get_ladder(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/ladders/<id>', methods = ['PUT'])
def update_ladder(id):
    response_body, keyed_args_dict = ascendancy.update_ladder(id, request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/ladders/<id>', methods = ['DELETE'])
def delete_ladder(id):
    response_body, keyed_args_dict = ascendancy.delete_ladder(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/challenges', methods = ['GET'])
def get_challenges():
    response_body, keyed_args_dict = ascendancy.get_challenges()
    return Response(response_body, **keyed_args_dict)

@app.route('/challenges', methods = ['POST'])
def new_challenge():
    response_body, keyed_args_dict = ascendancy.new_challenge(request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/challenges/<id>', methods = ['GET'])
def get_challenge(id):
    response_body, keyed_args_dict = ascendancy.get_challenges(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/challenges/<id>', methods = ['PUT'])
def update_challenge(id):
    response_body, keyed_args_dict = ascendancy.update_challenge(id, request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/challenges/<id>', methods = ['DELETE'])
def delete_challenge(id):
    response_body, keyed_args_dict = ascendancy.delete_challenge(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitors', methods = ['GET'])
def get_competitors():
    response_body, keyed_args_dict = ascendancy.get_competitors()
    return Response(response_body, **keyed_args_dict)

@app.route('/competitors', methods = ['POST'])
def new_competitor():
    response_body, keyed_args_dict = ascendancy.new_competitor(request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitors/<id>', methods = ['GET'])
def get_competitor(id):
    response_body, keyed_args_dict = ascendancy.get_competitors(id)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitors/<id>', methods = ['PUT'])
def update_competitor(id):
    response_body, keyed_args_dict = ascendancy.update_competitor(id, request.form)
    return Response(response_body, **keyed_args_dict)

@app.route('/competitors/<id>', methods = ['DELETE'])
def delete_competitor(id):
    response_body, keyed_args_dict = ascendancy.delete_competitor(id)
    return Response(response_body, **keyed_args_dict)

if __name__ == '__main__':
    app.run(debug=True)

