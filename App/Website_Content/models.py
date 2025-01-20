from App import db

# Association Tables for Many-to-Many Relationships
page_section = db.Table('page_section',
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True)
)

section_asset = db.Table('section_asset',
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.Column('asset_id', db.Integer, db.ForeignKey('asset.id'), primary_key=True)
)

section_content = db.Table('section_content',
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.Column('content_id', db.Integer, db.ForeignKey('content.id'), primary_key=True)
)

page_pricing = db.Table('page_pricing',
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('pricing_id', db.Integer, db.ForeignKey('pricing.id'), primary_key=True)
)

page_benefits = db.Table('page_benefits',
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True),
    db.Column('benefits_id', db.Integer, db.ForeignKey('benefits.id'), primary_key=True)
)

pricing_option = db.Table('pricing_option',
    db.Column('pricing_id', db.Integer, db.ForeignKey('pricing.id'), primary_key=True),
    db.Column('option_id', db.Integer, db.ForeignKey('option.id'), primary_key=True)
)

option_feature = db.Table('option_feature',
    db.Column('option_id', db.Integer, db.ForeignKey('option.id'), primary_key=True),
    db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

benefit_listing = db.Table('benefit_listing',
    db.Column('benefits_id', db.Integer, db.ForeignKey('benefits.id'), primary_key=True),
    db.Column('benefit_id', db.Integer, db.ForeignKey('benefit.id'), primary_key=True)
)


# Page Model
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    slug = db.Column(db.String(255), nullable=False, index=True)

    sections = db.relationship('Section', secondary=page_section, backref='page')
    pricing_items = db.relationship('Pricing', secondary=page_pricing, backref='page')
    benefits = db.relationship('Benefits', secondary=page_benefits, backref='page')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'sections': [section.to_dict() for section in self.sections],
            'pricing_items': [pricing.to_dict() for pricing in self.pricing_items],
            'benefits': [benefit.to_dict() for benefit in self.benefits]
        }

# Section Model
class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    section_text = db.Column(db.Text, nullable=True)
    
    assets = db.relationship('Asset', secondary=section_asset, backref='section')
    content_blocks = db.relationship('Content', secondary=section_content, backref='section')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'section_text': self.section_text,
            'assets': [asset.to_dict() for asset in self.assets],
            'content_blocks': [content.to_dict() for content in self.content_blocks]
        }

# Asset Model
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    class_name = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(255), nullable=False, index=True)
    asset_content = db.Column(db.Text, nullable=False)
    asset = db.Column(db.String(255), nullable=False, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'class_name': self.class_name,
            'type': self.type,
            'asset_content': self.asset_content,
            'asset': self.asset
        }

# Content Model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    class_name = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(255), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'class_name': self.class_name,
            'type': self.type,
            'content': self.content
        }

# Pricing Model
class Pricing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    
    options = db.relationship('Option', secondary=pricing_option, backref='pricing')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'options': [option.to_dict() for option in self.options]
        }

# Option Model
class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subscription_duration = db.Column(db.String(255), nullable=False, index=True)
    price = db.Column(db.Float)
    ideal_audience = db.Column(db.Text, nullable=False)
    class_name = db.Column(db.Text, nullable=True)
    saving = db.Column(db.Integer)
    action = db.Column(db.String(255), nullable=False, index=True)

    features = db.relationship('Feature', secondary=option_feature, backref='option')
    
    def to_dict(self):
        return {
            'id': self.id,
            'subscription_duration': self.subscription_duration,
            'price': self.price,
            'ideal_audience': self.ideal_audience,
            'class_name': self.class_name,
            'saving': self.saving,
            'action': self.action,
            'features': [feature.to_dict() for feature in self.features]
        }

# Feature Model
class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature = db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'feature': self.feature
        }

# Benefits Model
class Benefits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False, index=True)
    content = db.Column(db.Text, nullable=True)
    
    benefit_listing = db.relationship('Benefit', secondary=benefit_listing, backref='benefits')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'benefit_listing': [benefit.to_dict() for benefit in self.benefit_listing]
        }

# Benefit Model
class Benefit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=True, index=True)
    comparison = db.Column(db.Text, nullable=False)
    benefit = db.Column(db.Text, nullable=False)
    class_name = db.Column(db.Text, nullable=True)
    top_class_name = db.Column(db.Text, nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'comparison': self.comparison,
            'benefit': self.benefit,
            'class_name': self.class_name,
            'top_class_name': self.top_class_name
        }
