from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World from Flask"


@app.route('/')
def index():
    #return render_template('index.html')
    return ("damn it")

@app.route('/blog')
def blog():
    # return render_template('about.html')
    return ("some blog bullshit")

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
