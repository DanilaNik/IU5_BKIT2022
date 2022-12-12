from flask import Flask
import generator

app = Flask('fibonacci sequences')

@app.route('/')
def main_page():
    return "<h1>Educational project flask app!</h1>"

@app.route('/<int:n>')
def get_sequence(n):
    return list(generator.fib(n))

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Oops! Try to write after URL /your_number</h1>"