from App import db

page_content = db.Table('page_content',
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('content_id', db.Integer, db.ForeignKey('content.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),nullable=False,index=True)

    contents = db.relationship('Content', secondary=page_content, backref='page')

class Content(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    section = db.Column(db.String(255),nullable=False,index=True)
    content = db.Column(db.String(255))