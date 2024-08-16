from App import db
from werkzeug.security import generate_password_hash,check_password_hash

class AdminUser(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable=False,index=True)
    email = db.Column(db.String(255),nullable=False,index=True)
    pass_secure = db.Column(db.String(255))
    is_superuser = db.Column(db.Boolean,default=False)
    is_admin = db.Column(db.Boolean,default=False)
    is_staff = db.Column(db.Boolean,default=False)

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
    
    def createsuperuser(email,username,password):
        admin = AdminUser(
            email = email,
            username = username,
            password = password,
        )
        admin.is_superuser = True
        admin.is_admin = True
        admin.is_staff = True

        db.session.add(admin)
        db.session.commit()
        return admin
    
    def account(id):
        account = AdminUser.query.filter_by(id=id).first()
        return account