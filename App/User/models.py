from App import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable=False,index=True)
    email = db.Column(db.String(255),nullable=True,index=True) 
    pass_secure = db.Column(db.String(255))

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