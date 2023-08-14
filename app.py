#import newrelic.agent

from flask import Flask, request
from flask import render_template

#newrelic.agent.initialize('newrelic.ini')
app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todos.append(todo)
    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.run(debug=True)
