from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    mylist = [10, 20, 30, 40, 50]
    return render_template('index.html', mylist=mylist)


@app.route('/other')
def other():
    some_text = 'Hi World'
    return render_template('other.html', some_text=some_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
