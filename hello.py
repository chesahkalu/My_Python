from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    
    
# on terminal enter = 'export FLASK_APP=hello.py' to set the file to be run as the flask app
# on terminal enter = 'flask run' to run the flask app