from flask import Flask, request, jsonify, render_template
from model import model
from scraper import handleURL
import json

application = Flask(__name__)


""" @application.route('/', methods=['GET'])
def home_page():
    return will_stuff


@application.route('/website_input', methods=['POST'])
def handle_website_input():
    # grab the input
    return model(inp) """
@application.route('/')
def hello_world():
    return 'Hello, World! Amrith'

def hyper_partisan():
    if request.method == 'POST':
        input = request.form.get('text')
        return '<h1> donny is {} </h1>'.format(input)

    return '''<form method="POST"> 
    parsed_text <input type = "text" name = "text">
    <input type = "submit">
    </form>'''

@application.route('/homepage', methods = ['POST', 'GET'])
def fetch_homepage():
    return render_template("index.html")


@application.route('/json', methods = ['POST'])
def handle_json():
    # data = request.form
    data = json.loads(request.get_data())
    parsedText = data['parsedText']
    text = handle_url(parsedText)
    return text

def handle_url(url):
    text = handleURL(url)
    return text

# def model(text):
#     bias = model(text)
#     return bias

if __name__ == '__main__':
    application.run(debug = True, port=8088)