from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from todo.sql_commands import get_all_values, insert_value, update_value, delete_by_id

app = Flask(__name__)

########################
#### DATABASE SETUP ####
########################

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mitko123@localhost/todo-db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)


########################
#### API RESOURCES #####
########################

@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    all_tasks = get_all_values()
    return {'result': all_tasks}


@app.route('/api/task', methods=['POST'])
def add_task():
    title = request.get_json()['title']
    insert_value(title)
    result = {'title': title}
    return {'result': result}


@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    title = request.get_json()['title']
    update_value(title, id)
    result = {'title': title}
    return {'result': result}


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    delete_by_id(id)
    result = {'message': 'record deleted'}
    return {'result': result}
