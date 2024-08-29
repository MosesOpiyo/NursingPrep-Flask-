from App import db

page_section = db.Table('page_section',
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True)
)

section_asset = db.Table('section_asset',
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.Column('asset_id', db.Integer, db.ForeignKey('asset.id'), primary_key=True)
)

section_content = db.Table('section_content',
    db.Column('section_id',db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.Column('content_id',db.Integer, db.ForeignKey('content.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)
    slug = db.Column(db.String(255),nullable=False,index=True)

    sections = db.relationship('Section', secondary=page_section, backref='page')

class Section(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)

    assets = db.relationship('Asset', secondary=section_asset, backref='section')
    content_blocks = db.relationship('Content', secondary=section_content,backref='section')

class Asset(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)
    type = db.Column(db.String(255),nullable=False,index=True)
    asset = db.Column(db.String(255),nullable=False,index=True)

class Content(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)
    type = db.Column(db.String(255),nullable=False,index=True)
    content = db.Column(db.Text,nullable=False)
