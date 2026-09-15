from flask import Flask,jsonify


studentrecord = Flask(__name__)

students = [
    { 'id': 1, 'name': 'John Doe', 'age': 20, 'programme': 'Computer Science' },
    { 'id': 2, 'name': 'Jane Smith', 'age': 22, 'programme': 'Mathematics' },
    { 'id': 3, 'name': 'Michael Johnson', 'age': 21, 'programme': 'Physics' },
    { 'id': 4, 'name': 'Emily Davis', 'age': 19, 'programme': 'Biology' },
    { 'id': 5, 'name': 'William Brown', 'age': 23, 'programme': 'Chemistry' }
]

@studentrecord.route('/api/students', methods=['GET'])

@studentrecord.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    for i in students:
        if i['id'] == id:
            return jsonify(i)
    return jsonify({'error': 'Student not found'}),


@studentrecord.route('/api/students', methods=['POST'])
def add_student():
    new_student = {
        'id': 6,
        'name': 'Sarah Wilson',
        'age': 20,
        'programme': 'Mathematics'
    }
    students.append(new_student)
    return jsonify(new_student), 201

@studentrecord.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    for i in students:
        if i['id'] == id:
            i['name'] = 'Updated Name'
            
            i['age'] = 25
            i['programme'] = 'Updated Programme'
            return jsonify(i)
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    studentrecord.run(debug=True)



