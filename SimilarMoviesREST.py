import flask
from flask import request, jsonify
from getSimilar import findSimilar
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/getSimilarMovies', methods=['GET'])
@cross_origin()
def home():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return findSimilar(id)


app.run()
