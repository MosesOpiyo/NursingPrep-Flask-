from App import db
from flask_restful import request
from ... import lms
from flask import jsonify
from flask_jwt_extended import jwt_required
from ...models import Course, Module, Topic, Lesson, Quiz

class AdminCourseWork:
   @lms.route('/course/<string:type>',methods=['GET'])
   @jwt_required
   def edit_course(model_name, item_id):
        # Mapping model name to actual SQLAlchemy model
        model_mapping = {
            'course': Course,
            'module': Module,
            'topic': Topic,
            'lesson': Lesson,
            'quiz': Quiz
        }
        
        # Check if model exists
        if model_name not in model_mapping:
            return jsonify({'status': 'error', 'message': 'Invalid model name'}), 400
        
        model = model_mapping[model_name]

        # Retrieve the item from the database
        item = model.query.get(item_id)
        if not item:
            return jsonify({'status': 'error', 'message': 'Item not found'}), 404

        # Get request data
        data = request.json

        # Update fields dynamically
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        
        try:
            db.session.commit()
            return jsonify({'status': 'success', 'message': f'{model_name} updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'status': 'error', 'message': str(e)}), 500