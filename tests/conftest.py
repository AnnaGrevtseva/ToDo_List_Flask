import pytest
from app.models import Todo
from app.models import app


@pytest.fixture()
def task_todo():
    task_todo = Todo('sleep', False)
    return task_todo


@pytest.fixture()
def test_client():
    flask_app = app
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
