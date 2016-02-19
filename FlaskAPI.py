import config
from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from models import Item, Base
from sqlalchemy.engine.url import URL
app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = URL(**config.DATABASE)
# app.config.from_object('config')

db = SQLAlchemy(app)

# Base.metadata.drop_all(bind=db.engine)
Base.metadata.create_all(bind=db.engine)

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Item, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

app.debug = True
if __name__ == '__main__':
  app.run()
