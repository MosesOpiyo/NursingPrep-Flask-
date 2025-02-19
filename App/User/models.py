from App import db
from sqlalchemy import Enum
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable=False,index=True)
    email = db.Column(db.String(255),nullable=True,index=True)
    phone_number = db.Column(db.String(20), nullable=True)
    role = db.Column(Enum('Student','Tutor','Admin','SuperAdmin', name='user_role_enum'), nullable=False, index=True)
    pass_secure = db.Column(db.String(255))

    is_superadmin = db.Column(db.Boolean,default=False)
    is_admin = db.Column(db.Boolean,default=False)
    is_tutor = db.Column(db.Boolean,default=False)

    __table_args__ = (
        db.UniqueConstraint('username', name='unique_username_constraint'),
        db.UniqueConstraint('email', name='unique_email_constraint'),
    )
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'Account {self.username}'