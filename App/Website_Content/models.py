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

page_pricing = db.Table('page_pricing',
    db.Column('page_id',db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('pricing_id',db.Integer, db.ForeignKey('pricing.id'), primary_key=True)
)

page_benefits = db.Table('page_benefits',
    db.Column('page_id',db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('benefits_id',db.Integer, db.ForeignKey('benefits.id'), primary_key=True)
)

pricing_option = db.Table('pricing_option',
    db.Column('pricing_id',db.Integer, db.ForeignKey('pricing.id'), primary_key=True),
    db.Column('option_id',db.Integer, db.ForeignKey('option.id'), primary_key=True)
)

option_feature = db.Table('option_feature',
    db.Column('option_id',db.Integer, db.ForeignKey('option.id'), primary_key=True),
    db.Column('feature_id',db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

benefit_listing = db.Table('benefit_listing',
    db.Column('benefits_id',db.Integer, db.ForeignKey('benefits.id'), primary_key=True),
    db.Column('benefit_id',db.Integer, db.ForeignKey('benefit.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)
    slug = db.Column(db.String(255),nullable=False,index=True)

    sections = db.relationship('Section', secondary=page_section, backref='page')
    pricing_items = db.relationship('Pricing', secondary=page_pricing, backref='page')
    benefits = db.relationship('Benefits', secondary=page_benefits , backref='page')
        
class Section(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),nullable=False,index=True)
    title = db.Column(db.String(255),nullable=False,index=True)
    section_text = db.Column(db.Text,nullable=True)
    assets = db.relationship('Asset', secondary=section_asset, backref='section')
    content_blocks = db.relationship('Content', secondary=section_content,backref='section')

class Asset(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)
    class_name = db.Column(db.Text,nullable=True)
    type = db.Column(db.String(255),nullable=False,index=True)
    asset_content = db.Column(db.Text,nullable=False)
    asset = db.Column(db.String(255),nullable=False,index=True)

class Content(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable=False,index=True)
    class_name = db.Column(db.Text,nullable=True)
    type = db.Column(db.String(255),nullable=False,index=True)
    content = db.Column(db.Text,nullable=False)

class Pricing(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    title = db.Column(db.String(255),nullable=False,index=True)
    content = db.Column(db.Text,nullable=False)
    
    options = db.relationship('Option', secondary=pricing_option,backref='pricing')

class Option(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    subscription_duration = db.Column(db.String(255),nullable=False,index=True)
    price = db.Column(db.Float)
    ideal_audience = db.Column(db.Text,nullable=False)
    class_name = db.Column(db.Text,nullable=True)
    saving = db.Column(db.Integer)
    action = db.Column(db.String(255),nullable=False,index=True)

    features = db.relationship('Feature', secondary=option_feature,backref='option')

class Feature(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    feature = db.Column(db.Text,nullable=False)

class Benefits(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    title = db.Column(db.String(255),nullable=False,index=True)
    content = db.Column(db.Text,nullable=True)
    
    benefit_listing = db.relationship('Benefit', secondary=benefit_listing,backref='benefits')

class Benefit(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    type = db.Column(db.String(255),nullable=True,index=True)
    comparison = db.Column(db.Text,nullable=False)
    benefit = db.Column(db.Text,nullable=False)
    class_name = db.Column(db.Text,nullable=True)
    top_class_name = db.Column(db.Text,nullable=True)



