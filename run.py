from flask import Flask
from flask_REST_API import app


if __name__ == '__main__':
    app.run(debug=True, port=5001)