# Flask RESTful API with CRUD Operations and JWT Authentication

This project is a RESTful API built using Flask that allows you to perform CRUD (Create, Read, Update, Delete) operations on a database of users. The API also includes user authentication using JSON Web Tokens (JWT).

## Features

- **User Registration**: Register new users with secure password hashing.
- **User Login**: Authenticate users with JWT for secure access.
- **CRUD Operations**: Create, read, update, and delete user data.
- **JWT Authentication**: Protect routes with JWT, ensuring only authenticated users can access certain endpoints.

## Technologies Used

- **Flask**: Micro web framework used to build the API.
- **SQLAlchemy**: ORM (Object-Relational Mapping) library for database operations.
- **JWT (JSON Web Tokens)**: Used for user authentication.
- **SQLite**: Lightweight database for storing user data.

## Getting Started

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/flask-crud-jwt-api](https://github.com/itsEkramah/DEP_Flask-RESTful-API-with-CRUD-Operations.git
    cd flask-crud-jwt-api
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python app.py
    ```

    The application will start on `http://localhost:5000`.

Here’s the updated section with real Pakistani names:

### API Endpoints

- **POST /register**: Register a new user.
  - Request: `{"name": "Ali Khan", "email": "alikhan@example.pk", "password": "password123"}`
  - Response: `{"message": "User registered successfully"}`

- **POST /login**: Authenticate a user and return a JWT.
  - Request: `{"email": "alikhan@example.pk", "password": "password123"}`
  - Response: `{"access_token": "your_jwt_token"}`

- **GET /users**: Retrieve all users (JWT required).
  - Response: `[{"id": 1, "name": "Ali Khan", "email": "alikhan@example.pk"}, ...]`

- **GET /users/<id>**: Retrieve a specific user by ID (JWT required).
  - Response: `{"id": 1, "name": "Ali Khan", "email": "alikhan@example.pk"}`

- **POST /users**: Create a new user (JWT required).
  - Request: `{"name": "Sara Ahmed", "email": "saraahmed@example.pk", "password": "password123"}`
  - Response: `{"message": "User created successfully"}`

- **PUT /users/<id>**: Update an existing user's information (JWT required).
  - Request: `{"name": "Bilal Raza", "email": "bilalraza@example.pk", "password": "newpassword123"}`
  - Response: `{"message": "User updated successfully"}`

- **DELETE /users/<id>**: Delete a user by ID (JWT required).
  - Response: `{"message": "User deleted successfully"}`
```
### Authentication

The API uses JWT for authentication. To access protected routes, include the JWT token in the `Authorization` header as follows:






### Database

This project uses SQLite as the database. The database file (`users.db`) will be automatically created in the root directory when you run the application for the first time.

### Running the Tests

To run tests, you can use a tool like `pytest`. Make sure to set up your testing environment with the necessary configurations before running the tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## Acknowledgements

- Flask Documentation: [Flask](https://flask.palletsprojects.com/)
- SQLAlchemy Documentation: [SQLAlchemy](https://www.sqlalchemy.org/)
- JWT Documentation: [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)


