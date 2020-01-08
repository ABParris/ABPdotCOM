from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('home.html')

@application.route('/blog')
def blog():
    return render_template('blogDisplay.html')

if __name__=='__main__':
    application.run(debug=True, port=8080)