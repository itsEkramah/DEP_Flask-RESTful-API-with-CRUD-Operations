from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ngrok import run_with_ngrok

# Initialize the Flask app
app = Flask(__name__)
run_with_ngrok(app)  # Add ngrok support to expose the app via a public URL

# Configure the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a more secure key

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create the database and add example data
with app.app_context():
    db.create_all()

    if User.query.count() == 0:
        example_users = [
            {'name': 'Asad Imam', 'email': 'asadimam@example.pk', 'password': 'password123'},
            {'name': 'Samiullah', 'email': 'samiullah@example.pk', 'password': 'password123'},
            {'name': 'Fahad Raza', 'email': 'fahadraza@example.pk', 'password': 'password123'},
            {'name': 'Ali Malik', 'email': 'alimalik@example.pk', 'password': 'password123'},
            {'name': 'Bilal Hussain', 'email': 'bilalhussain@example.pk', 'password': 'password123'},
            {'name': 'Zainab Saeed', 'email': 'zainabsaeed@example.pk', 'password': 'password123'}
        ]
        for user_data in example_users:
            hashed_password = generate_password_hash(user_data['password'], method='pbkdf2:sha256')
            new_user = User(name=user_data['name'], email=user_data['email'], password=hashed_password)
            db.session.add(new_user)
        db.session.commit()

# Define the routes for CRUD operations and authentication

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"msg": "Bad email or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

@app.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        result.append(user_data)
    return jsonify(result)

@app.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user_data = {'id': user.id, 'name': user.name, 'email': user.email}
    return jsonify(user_data)

@app.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    if 'password' in data:
        user.password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

# Run the app
if __name__ == '__main__':
    app.run()
