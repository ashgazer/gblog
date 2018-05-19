from flask import Flask
app = Flask(__name__)

# from core import views
from  flask import render_template , url_for


@app.route('/')
def index():
    return render_template('index.html')
    #return ("damn it")

@app.route('/blog')
def blog():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
