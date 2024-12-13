from flask import Flask, request, make_response
app = Flask(__name__)



@app.route('/')
def index():
    return "<h1>Hi, ManojKumar</h1>"



@app.route('/hello')
def hello():
    response = make_response("Hello, World")
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"

# @app.route('/add/<num1>/<num2>')
# it will concatenate num1 and num2 because it consider both are strings.
# def add(num1, num2):
    # return f"{num1}+{num2} = {num1+num2}"


@app.route('/add/<int:num1>/<int:num2>')
# it will concatenate num1 and num2 because it considers both are strings.
def add(num1, num2):
    return f"{num1}+{num2} = {num1 + num2}"


@app.route('/handle_url_params')
# Url Parameters Handling.
def handle_prams():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return f"Some Parameter is missing"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)