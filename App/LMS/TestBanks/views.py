from App import db
from .. import lms
from flask import jsonify
from flask_jwt_extended import jwt_required
import pandas as pd

from ..models import TestBankQuestion,QuestionChoice

class NewAndUpdateClass:
    @lms.route('/banks/new-question',methods=['POST'])
    @jwt_required()
    def create_question(request):
        # Check if the request is JSON data
        if request.is_json:
            data = request.get_json()

            # Handle multiple entries if data is a list
            if isinstance(data, list):
                questions = []
                for entry in data:
                    result = TestBankQuestion._process_question_entry(entry)
                    if result['status'] == 'success':
                        questions.append(result['question'])
                    else:
                        return jsonify({'error': result['message']}), 400

                db.session.commit()
                return jsonify({'questions': questions, 'message': 'Multiple questions created successfully'}), 201

            # Handle single entry if data is a dictionary
            elif isinstance(data, dict):
                result = NewAndUpdateClass._process_question_entry(data)
                if result['status'] == 'success':
                    db.session.commit()
                    return jsonify(result['question']), 201
                else:
                    return jsonify({'error': result['message']}), 400
            else:
                return jsonify({'error': 'Invalid JSON format'}), 400

        # Check if the request has a file
        elif 'file' in request.files:
            file = request.files['file']

            # Check if the file is a CSV
            if file.filename.endswith('.csv'):
                try:
                    # Read the CSV file using pandas
                    df = pd.read_csv(file)
                    
                    # Check if required columns exist
                    required_columns = ['question_text', 'difficulty', 'topic', 'correct_answer', 'choice_1', 'choice_2', 'choice_3', 'choice_4']
                    if not all(column in df.columns for column in required_columns):
                        return jsonify({'error': 'CSV file must contain question_text, difficulty, topic, correct_answer, choice_1, choice_2, choice_3, and choice_4 columns'}), 400
                    
                    questions = []
                    for _, row in df.iterrows():
                        entry = {
                            'question_text': row['question_text'],
                            'difficulty': row['difficulty'],
                            'topic': row['topic'],
                            'correct_answer': row['correct_answer'],
                            'choices': [
                                row['choice_1'], row['choice_2'], row['choice_3'], row['choice_4']
                            ]
                        }
                        result = NewAndUpdateClass._process_question_entry(entry)
                        if result['status'] == 'success':
                            questions.append(result['question'])
                        else:
                            return jsonify({'error': result['message']}), 400
                    
                    db.session.commit()
                    return jsonify({'questions': questions, 'message': 'Questions created from CSV successfully'}), 201
                
                except Exception as e:
                    return jsonify({'error': f'Failed to process CSV: {str(e)}'}), 500
            else:
                return jsonify({'error': 'Only CSV files are supported'}), 400
        
        else:
            return jsonify({'error': 'Request must contain JSON data or a CSV file'}), 400
