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
    """
    

    input_text = request.args.get("input_text")

    return jsonify(Entered_text=input_text)



if __name__  == '__main__':    
    app.debug = True
    app.run(host="0.0.0.0",port=5777)
    #http://localhost:5777/apidocs/#/get_movie_details
