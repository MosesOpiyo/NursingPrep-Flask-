from flask import request,jsonify
from flask_restful import reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from App import db,cache
from ...User import user
from ..models import User
from ..schema import ProfileSchema
from ...authentication import user_authentication

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=False)
user_parser.add_argument('username', type=str, required=False)

@user.route('/Authentication/Profile',methods=['GET'])
@jwt_required()
@cache.cached(timeout=300, key_prefix=lambda: f"profile_{get_jwt_identity()}")
def get_profile():
    schema = ProfileSchema()
    current_user_id = get_jwt_identity()
    user = User.query.with_entities(User.username, User.email).filter_by(id=current_user_id).first()
    if user:
        user_data = schema.dump(user)
        return user_data, 200
    else:
        return jsonify({'msg': 'User not found'}), 404
    

@user.route('/Authentication/UpdateProfile',methods=['PUT'])
@jwt_required()
def update_profile():
    args = user_parser.parse_args()
    email = args['email']
    username = args['username']
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if user:
        if username:
            user.username = username
        if email:
            user.email = email
        db.session.commit()
        return jsonify({
            'message': 'User updated successfully',
            'user': {
                'username': user.username,
                'email': user.email
            }
        }), 200
    return jsonify({'msg': 'User not found'}), 404
    






