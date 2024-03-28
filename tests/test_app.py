from flask import Flask

def test_app(app_setup):
    assert isinstance(app_setup, Flask)
    assert app_setup.config['TESTING'] is True
    assert app_setup.config['DEBUG'] is True