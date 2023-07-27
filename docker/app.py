import spacy
from flask import Flask, request

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    print("test")


if __name__ == '__main__':
    app.run(debug=True)
