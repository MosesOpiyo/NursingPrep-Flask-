from App import db
from ....LMS import lms
from sqlalchemy.orm import joinedload
from flask import request,jsonify
from ...models import Course
from .schema import CourseSchema

class CourseWork:
    @lms.route('/course/<string:type>',methods=['GET'])
    def getCourseWork():
        # Pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Efficient loading using joinedload
        courses = Course.query.options(
            joinedload(Course.inclusions),
            joinedload(Course.modules).joinedload('topics').joinedload('lessons')
        ).paginate(page=page, per_page=per_page, error_out=False)
        
        # Serializing the data
        data = []
        course_schema = CourseSchema()
        for course in courses.items:
            course_data = {
                'id': course.id,
                'type': course.type,
                'course_name': course.course_name,
                'introduction_message': course.introduction_message,
                'details': course.details,
                'inclusions': [inc.inclusion for inc in course.inclusions],
                'modules': []
            }
            
            for module in course.modules:
                module_data = {
                    'id': module.id,
                    'module_name': module.module_name,
                    'topics': []
                }
                
                for topic in module.topics:
                    topic_data = {
                        'id': topic.id,
                        'topic_name': topic.topic_name,
                        'lessons': [{'id': lesson.id, 'lesson_name': lesson.lesson_name} for lesson in topic.lessons]
                    }
                    module_data['topics'].append(topic_data)
                
                course_data['modules'].append(module_data)
            
            data.append(course_data)
        
        return jsonify({
            'status': 'success',
            'data': course_schema.dump(data),
            'page': courses.page,
            'total_pages': courses.pages,
            'total_items': courses.total
        })