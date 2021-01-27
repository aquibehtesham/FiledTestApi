from flask import Flask, request, jsonify
from flasgger import Swagger


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.debug = True

swagger = Swagger(app)

@app.route('/hello_world', methods=['GET','POST'])
def say_hello():
    '''
    this is test route for flask app
    '''
    return "Hello World!"


if __name__  == '__main__':
    # app.config["JSON_SORT_KEYS"] = False
    app.debug = True
    app.run(host="0.0.0.0",port=5777)
    #http://localhost:5777/apidocs/#/get_movie_details
