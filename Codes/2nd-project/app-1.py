import pandas as pd
from flask import Flask, render_template, request, url_for
app = Flask(__name__, template_folder='templates-1')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index-1.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'manoj' and password == 'password':
            return 'Success'
        else:
            return 'Failure'


@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)