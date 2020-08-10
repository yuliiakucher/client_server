from flask import Flask
from flask_restful import Api
from .resources import User
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

api = Api(app)
api.add_resource(User, '/user', '/user/<string:email>')
