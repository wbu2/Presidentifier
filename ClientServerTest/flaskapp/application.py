from flask import Flask, request, jsonify, render_template
from scraper import handleURL
import json
from match_my_voice import Model

application = Flask(__name__)


def hyper_partisan():
    if request.method == 'POST':
        input = request.form.get('text')
        return '<h1> donny is {} </h1>'.format(input)

    return '''<form method="POST"> 
    parsed_text <input type = "text" name = "text">
    <input type = "submit">
    </form>'''

@application.route('/website_endpoint', methods = ['POST'])
def handle_input():
    print(request.get_data())
    text = str(request.get_data()).split('=')[1]
    user = model(text)
    return user

@application.route('/', methods = ['POST', 'GET'])
def fetch_homepage():
    return render_template("index.html")


@application.route('/json', methods = ['POST'])
def handle_json():
    # data = request.form
    data = json.loads(request.get_data())
    parsedText = data['parsedText']
    text = handle_url(parsedText)
    print(text)
    user = model(text)
    return user

def handle_url(url):
    text = handleURL(url)
    return text

def model(text):
    us = Model()
    user = us.predict(text)
    return user


if __name__ == '__main__':
    application.run(debug = True, port=8088)