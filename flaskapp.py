from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/userlist')
def userlist():
    response = jsonify({'my':'data'})
    response.set_cookie('userID', 'cookie_from_centos_os', domain='.my-example.net')
    return response

@app.route('/userlist2')
def userlist2():
    response = jsonify({'some':'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.set_cookie('userID', 'cookie_from_centos_os2');
    return response

@app.route('/checkcookie')
def checkcookie():
    name = request.cookies.get('userID')
    return '<h1>'+name+'</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

