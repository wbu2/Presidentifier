from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hyper_partisan', methods=['POST', 'GET'])

#def hyper_partisan():
 #   if request.method == 'POST':
  #      input = request.form.get('text')
   #     return '<h1> donny is {} </h1>'.format(input)

    #return '''<form method="POST"> 
    #parsed_text <input type = "text" name = "text">
    #<input type = "submit">
    #</form>'''

@app.route('/json', methods = ['POST', 'GET'])
def handle_json():
    print("GOT A POST")
    print(request.form)
    data = request.form
    # data = request.get_json()
    parsedText = data['parsedText']
    return jsonify({'parsedText': parsedText, 'hyperPartisan': True})


if __name__ == '__main__':
    app.run(debug = True, port=8088)