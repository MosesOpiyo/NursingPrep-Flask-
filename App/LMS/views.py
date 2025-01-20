from App import db
from . import lms
from flask import jsonify
from flask_jwt_extended import jwt_required
import csv
from io import StringIO

from .models import Course
from ..User.get_user import get_user
from .schema import CourseInfoSchema,CourseSchema

from .models import Module,UserProgress
from .learning_content import get_course

class CourseWork:
    @lms.route('/course/<string:type>',methods=['GET'])
    def getCourses(type):
        data = {}
        course_schema = CourseInfoSchema(many=True)
        course_data = Course.query.filter_by(type=type).all()
        if course_data:
            course = course_schema.dump(course_data)
            data = course,200
        else:
            data = jsonify('Course not found'),404
        return data

    @lms.route('/course/<string:course>',methods=['GET'])
    def getCourseWork(course):
        data = {}
        course_schema = CourseSchema()
        course_data = Course.query.filter_by(course_name=course).first()
        if course_data:
            course = course_schema.dump(course_data)
            data = course,200
        else:
            data = jsonify('Course not found'),404
        return data
    
    @lms.route('/course/<string:course>',methods=['POST'])
    @jwt_required()
    def newModules(request,course):
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']

        # Ensure the file has a valid extension (optional)
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File must be a CSV'}), 400
        

        # Parse the CSV file
        file_content = StringIO(file.read().decode('utf-8'))
        csv_reader = csv.DictReader(file_content)

        # Retrieve the course
        course = Course.query.get(course)
        if not course:
            return jsonify({'error': 'Course not found'}), 404

        # Iterate through the CSV and assign modules
        for row in csv_reader:
            module_name = row.get('module_name')
            if module_name:
                # Check if the module already exists
                module = Module.query.filter_by(module_name=module_name).first()

                if not module:
                    # Create the module if it doesn't exist
                    module = Module(module_name=module_name)
                    db.session.add(module)

                # Assign the module to the course (many-to-many relationship)
                if module not in course.modules:
                    course.modules.append(module)

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'Modules successfully assigned to course'}), 200
    
class Progression:
    @lms.route('/progression/new-addition/<int:id>',methods=['GET'])
    @jwt_required()
    def newAddition(id):
        data = {}
        user = get_user()
        progression = UserProgress.query.filter_by(user=user).first()
        new_course = Course.query.filter_by(id=id).first()
        progression.course_progression.add(new_course)
        db.session.commit()
        data = jsonify('New course on going'),200
        return data
            

        