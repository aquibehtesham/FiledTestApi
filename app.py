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

@app.route('/test_service', methods=['GET'])
def test_service():
    """        
    API route to get Response
    ---
    tags:
      - Get Response from Test Service
    parameters:
        - name: input_text
          in: query
          type: string
          required: true
          description: Enter text to test the service api
    responses:
      500:
        description: Error Please enter the text data!
      200:
        description: Movie Details
        schema:
          id: Movie details (API Response)
          properties:
            Title:
              type: string
              description: The movie title
              default: 'NA'            
    """
    

    movie_name = request.args.get("Movie")

    print("movie name - ", movie_name)

    


    return jsonify(Title=movie_name)



if __name__  == '__main__':
    # app.config["JSON_SORT_KEYS"] = False
    app.debug = True
    app.run(host="0.0.0.0",port=5777)
    #http://localhost:5777/apidocs/#/get_movie_details
