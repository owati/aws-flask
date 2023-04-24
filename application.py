from flask import Flask

application = app = Flask(__name__)


@app.route("/")
def index() :
    return '''
    <h1>This is an aws application created with flask</h1>
    '''

if __name__ == "__main__":
    app.run(debug=True)