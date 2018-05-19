from flask import render_template , url_for


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    # return render_template('about.html')
    return ("some blog bullshit")

@app.route('/about')
def about():
    return render_template('about.html')