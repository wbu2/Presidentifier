from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Amrith'

@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '<h1>The language is {}. The framework is {}.</h1>'.format(language, framework) 
    return '''<form method="POST">
    Language <input type="text" name="language">
    Framework <input type="text" name="framework">
    <input type="submit">
    </form>'''

@app.route('/json_example', methods=['POST', 'GET'])
def json_example():
    print(request.args)
    data = request.get_json()
    parsedText = data['parsedText']
    return jsonify({'parsedText': parsedText, 'valid': True})


