from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User

@jwt_required
def get_user():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    return user