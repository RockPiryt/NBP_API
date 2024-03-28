import pytest

from NBP_API_project import create_app, db

@pytest.fixture
def app_setup():

    app = create_app("testing")

    with app.app_context():
        db.create_all()

    yield app

    # # # Remove test database path
    # app.config["DB_FILE_PATH"].unlink(missing_ok=True)

@pytest.fixture
def client_setup(app_setup):
    with app_setup.test_client() as client:
        yield client