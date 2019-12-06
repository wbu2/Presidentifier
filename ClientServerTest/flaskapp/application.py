from flask import Flask, request, jsonify
from model import model

application = Flask(__name__)


@application.route('/', methods=['GET'])
def home_page():
    return will_stuff


@application.route('/website_input', methods=['POST'])
def handle_website_input():
    # grab the input
    return model(inp)

@app.route('/hyper_partisan', methods=['POST', 'GET'])
def hyper_partisan():
    if request.method == 'POST':
        input = request.form.get('text')
        return '<h1> donny is {} </h1>'.format(input)

    return '''<form method="POST"> 
    parsed_text <input type = "text" name = "text">
    <input type = "submit">
    </form>'''

@app.route('/homepage', methods = ['POST', 'GET'])
def fetch_homepage():
    return render_template("home.html")


@application.route('/json', methods = ['POST'])
def handle_json():
    print("GOT A POST")
    print(request.form)
    data = request.form
    # data = request.get_json()
    parsedText = data['parsedText']
    return jsonify({'parsedText': parsedText, 'hyperPartisan': True})


if __name__ == '__main__':
    application.run(debug = True, port=8088)