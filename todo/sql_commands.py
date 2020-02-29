from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:mitko123@localhost/todo-db')


def get_all_values():
    all_tasks = engine.execute(f'SELECT * FROM tasks')
    list_tasks = [{'id': v[0], 'title': v[1]} for v in all_tasks]
    return list_tasks


def insert_value(title):
    engine.execute(f'INSERT INTO tasks (title) VALUES (\'{title}\')')


def update_value(title, row_id):
    engine.execute(f'UPDATE tasks SET title = \'{title}\' WHERE id = {row_id}')


def delete_by_id(row_id):
    engine.execute(f'DELETE FROM tasks WHERE id = {row_id}')
