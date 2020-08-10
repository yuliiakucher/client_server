from flask_restful import Resource, reqparse
from app.models import UserModel


class User(Resource):
    request = reqparse.RequestParser()
    request.add_argument('name', required=True, type=str, help='Name is not valid')
    request.add_argument('email', required=False, type=str, help='Email is not valid')

    def get(self, email):
        user = UserModel.get_by_email(email)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json(), 200
    def post(self):
        data = User.request.parse_args()
        if UserModel.get_by_email(data['email']):
            return {'message': 'Email already exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'user is created'}

    def delete(self, email):
        user = UserModel.get_by_email(email)
        user.delete_from_db()
        return {'message': 'User is deleted'}

    def put(self, email):
        data = User.request.parse_args()
        user = UserModel.get_by_email(email)
        if not user:
            user = UserModel(name=data['name'], email=email)
            user.save_to_db()
            return {'message': f'User with email {email }is created'}, 201
        user.name = data['name']
        user.save_to_db()
        return {'message': 'User`s name have been changed'}, 200


    def patch(self):
        return 'hi from patch'
