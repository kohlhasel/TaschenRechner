import flask
from flask import Flask
from waitress import serve
from flask_cors import CORS
from calcs import Taschenrechner



rechner = Taschenrechner()



def create_app():
    app = Flask(__name__)
    CORS(app)
    return app

APP = create_app()


@APP.route('/version')
def version_request():
    return {"version": "4.0 -- Lukas Kohlhase"}

@APP.route('/add', methods=['POST'])
def addition_request():
    requestinfos={key: value for key,value in flask.request.json.items()}
    return str(rechner.addition(requestinfos['wert1'],requestinfos['wert2']))

@APP.route('/sub', methods=['POST'])
def sub_request():
    requestinfos={key: value for key,value in flask.request.json.items()}
    return str(rechner.subtraktion(requestinfos['wert1'],requestinfos['wert2']))

@APP.route('/mul', methods=['POST'])
def mul_request():
    requestinfos={key: value for key,value in flask.request.json.items()}
    return str(rechner.multiplikation(requestinfos['wert1'],requestinfos['wert2']))

if __name__ == '__main__':

    serve(APP, port=8100)
