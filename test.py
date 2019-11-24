from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("index")
    return 'Hello, World!'

    # if __name__ == '__main__':

config = dict(
    debug=True,
    host='0.0.0.0',
    port=2000,
)

app.run(**config)
