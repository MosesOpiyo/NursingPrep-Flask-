import json
from App import db
from .models import Page, Section, Asset, Content, Pricing, Option, Feature, Benefits, Benefit

def load_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Load Pages
    for page_data in data['pages']:
        page = Page(
            title=page_data['title'],
            slug=page_data['slug']
        )
        db.session.add(page)
        db.session.commit()  # Commit here so we get the ID for relationships
        
        # Load Sections for each Page
        for section_data in page_data.get('sections', []):
            section = Section(
                name=section_data['name'],
                title=section_data['title'],
                section_text=section_data.get('section_text', '')
            )
            db.session.add(section)
            db.session.commit()
            
            page.sections.append(section)  # Add to the relationship
            db.session.commit()  # Commit the changes for this page-section relation

        # Load Pricing Items for each Page
        for pricing_data in page_data.get('pricing_items', []):
            pricing = Pricing(
                page_id=page.id,
                title=pricing_data['title'],
                content=pricing_data['content']
            )
            db.session.add(pricing)
            db.session.commit()

            for option_data in pricing_data.get('options', []):
                option = Option(
                    subscription_duration=option_data['subscription_duration'],
                    price=option_data['price'],
                    ideal_audience=option_data['ideal_audience'],
                    class_name=option_data.get('class_name', ''),
                    saving=option_data.get('saving', 0),
                    action=option_data['action']
                )
                db.session.add(option)
                db.session.commit()

                pricing.options.append(option)  # Add to the relationship
                db.session.commit()

        # Load Benefits for each Page
        for benefit_data in page_data.get('benefits', []):
            benefits = Benefits(
                page_id=page.id,
                title=benefit_data['title'],
                content=benefit_data.get('content', '')
            )
            db.session.add(benefits)
            db.session.commit()

            for benefit_listing_data in benefit_data.get('benefit_listing', []):
                benefit = Benefit(
                    type=benefit_listing_data['type'],
                    comparison=benefit_listing_data['comparison'],
                    benefit=benefit_listing_data['benefit'],
                    class_name=benefit_listing_data.get('class_name', ''),
                    top_class_name=benefit_listing_data.get('top_class_name', '')
                )
                db.session.add(benefit)
                db.session.commit()

                benefits.benefit_listing.append(benefit)  # Add to the relationship
                db.session.commit()

    # Optional: commit the final session to make sure all transactions are persisted
    db.session.commit()
