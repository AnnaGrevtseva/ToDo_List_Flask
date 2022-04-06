"""Module to control logic (add new tasks, mark to finish)"""

import enum
import logging
import threading
import webbrowser

from app.models import Todo, app, db
from app.settings import settings
from flask import flash, redirect, render_template, request, url_for


class StatusTask(str, enum.Enum):
    """Status for task"""

    ALL = 'all'
    FINISHED = 'finished'


@app.route('/')
def index():
    """Start page"""

    status = request.args.get('status')

    if StatusTask.ALL == status:
        incomplete_tasks = Todo.query.filter_by(complete=False).all()
        complete_tasks = Todo.query.filter_by(complete=True).all()

        return render_template(
            'index.html',
            incomplete=incomplete_tasks,
            complete=complete_tasks)

    if StatusTask.FINISHED == status:
        complete_tasks = Todo.query.filter_by(complete=True).all()

        return render_template(
            'index.html',
            complete=complete_tasks)

    incomplete_tasks = Todo.query.filter_by(complete=False).all()

    return render_template(
        'index.html',
        incomplete=incomplete_tasks)


@app.route('/add', methods=['POST'])
def add():
    """ Add new tasks"""

    todo = Todo(text=request.form['todoitem'], complete=False)

    if todo.text:
        # pylint: disable=no-member
        db.session.add(todo)
        db.session.commit()

        info_message = f'Item with id = {todo.task_id} added'
        logging.info(info_message)

        flash_message = f'ToDo task "{todo.text}" added'
        flash(flash_message)

    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    """Finished tasks"""

    todo = Todo.query.filter_by(task_id=int(todo_id)).first()
    todo.complete = True

    # pylint: disable=no-member
    db.session.commit()

    info_message = f'Item with id = {todo_id} finished'
    logging.info(info_message)

    return redirect(url_for('index'))


def run():
    """Run application"""

    db.create_all()

    url = settings.host_url
    timer_interval = 1.0
    threading.Timer(timer_interval, lambda: webbrowser.open(url)).start()

    app.run()
