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

@app.route('/get_movie_details')
def movie_details():
    """        
    parameters:
        - name: Movie
          in: query
          type: string
          required: true
          description: Enter Movie name as same as in IMDb website
    responses:
      500:
        description: Error Please enter the correct movie name as same as in Imdb website!
      200:
        description: Movie Details
        schema:
          id: Movie details (API Response)
          properties:
            Title:
              type: string
              description: The movie title
              default: 'NA'
            
            # Plot:
            #   type: string
            #   description: The movie plot
            #   default: 'NA'
            # Plot_Outline:
            #   type: string
            #   description: The movie plot-outline
            #   default: 'NA'
            # Synopsis:
            #   type: string
            #   description: The movie Synopsis
            #   default: 'NA'
    """
    

    movie_name = request.args.get("Movie")

    print("movie name - ", movie_name)

    


    return jsonify(Title=movie_name
                   # _="---  Plot  ---",
                   # Plot=plot,
                   # __="---  Plot Outline  ---",
                   # Plot_Outline=plot_outline,
                   # ___="---  synopsis  ---",
                   # Synopsis = synopsis
                   )



if __name__  == '__main__':
    # app.config["JSON_SORT_KEYS"] = False
    app.debug = True
    app.run(host="0.0.0.0",port=5777)
    #http://localhost:5777/apidocs/#/get_movie_details
