from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://34.132.34.71:27017/')
db = client['tasks_db']
tasks_collection = db['tasks']

@app.route('/')
def index():
    tasks = list(tasks_collection.find({}, {'_id': 0, 'task': 1}))
    return render_template('index.html', tasks=[task['task'] for task in tasks])

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks_collection.insert_one({'task': task})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks = list(tasks_collection.find({}, {'_id': 0, 'task': 1}))
    if 0 <= task_id < len(tasks):
        task_to_delete = tasks[task_id]['task']
        tasks_collection.delete_one({'task': task_to_delete})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
