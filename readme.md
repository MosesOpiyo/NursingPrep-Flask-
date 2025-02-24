# NursingPrepCentral

## Overview
NursingPrepCentral is a modular Learning Management System (LMS) for NursingPrepCentral.com. The system will serve TEAS, HESI, NCLEX, and Nursing School Exams modules, prioritizing the TEAS module in the initial phase. The LMS will feature AI-enhanced functionality, adaptive quizzes, robust CMS capabilities, modular architecture for institutional licensing, and advanced analytics.

## Features
- Authentication & User Management
- Extensive Modules: TEAS, HESI A2, NCLEX, Nursing School 
- Feature 3

<!-- ## Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/yourproject.git

# Navigate to the project directory
cd yourproject

# Install dependencies
npm install  # or pip install -r requirements.txt

# Start the application
npm start  # or python app.py
``` -->

## API Endpoints
### Authentication
#### Register a User
**Endpoint:** `POST /user/Authentication/<string:module>/Registration/`
**Description:** Registers a new user, create user billing, attach module plans
**Request Body:**
```json
{
  "username": "string",
  "email": "string",
  "role": "string",
  "password": "string"
}
```
**Response:**
```json
{
  "access": "Access Token", 
  "refresh": "Refresh Token"
}
```

#### Login
**Endpoint:** `POST /api/auth/login`
**Description:** Authenticates a user and returns a token.
**Request Body:**
```json
{
  "email": "string",
  "password": "string"
}
```
**Response:**
```json
{
  "access": "Access Token", 
  "refresh": "Refresh Token"
}
```

### User Management
#### Get User Profile
**Endpoint:** `GET /user/Authentication/Profile`
**Description:** Fetches the authenticated user's profile.
**Headers:**
```json
{
  "Authorization": "Bearer your_jwt_token"
}
```
**Response:**
```json
{
  "id": "integer",
  "username": "string",
  "email": "string"
}
```

### Additional Endpoints
Include other relevant endpoints for your project.

## Technologies Used
- Node.js / Express.js (or Flask, Django, etc.)
- MongoDB / PostgreSQL
- JWT Authentication
- Other relevant technologies

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## License
Specify the license type (e.g., MIT License).



