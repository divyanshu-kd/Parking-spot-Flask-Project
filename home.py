from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hi!</h1>'

if __name__ == '__main__':
    app.run()