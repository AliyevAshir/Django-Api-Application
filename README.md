# Employee Management App

## Overview

This application is designed for managing employees, their positions, and departments. It provides a comprehensive API for user management, department and position handling, and employee records.

## Database Structure

### Department
- **PK**: ID
- **Fields**:
  - name
  - created_at
  - updated_at

### Position
- **PK**: ID
- **Fields**:
  - name
  - salary
  - created_at
  - updated_at
- **FK**: department_id

### Employee
- **PK**: ID
- **Fields**:
  - name
  - surname
  - email
  - status
  - created_at
  - updated_at
- **FK**:
  - department_id
  - position_id

## Features

### User Management
1. User registration
2. User login

### Department Management
1. Save a department
2. Retrieve a specific department
3. Retrieve all departments
4. Edit a department
5. Delete a department

### Position Management
1. Save a position
2. Retrieve a specific position
3. Retrieve all positions
4. Edit a position
5. Delete a position

### Employee Management
1. Save an employee
2. Retrieve a specific employee
3. Retrieve all employees
4. Edit an employee
5. Delete an employee

## Technologies Used
1. Django
2. Django Rest Framework
3. Celery
4. JSON Web Tokens (JWT)
5. PostgreSQL

## Technical Structure

1. Users must register with token authentication. Each user must have at least one role (admin, user).
2. The `/register` and `/login` endpoints are open to everyone. All other endpoints require an authenticated user.
3. DELETE endpoints can only be accessed by users with the "ADMIN" role.
4. Multilanguage support must be implemented (Azerbaijani and English are sufficient). Response data for position and department names should return in the appropriate language.
5. API documentation is required (Swagger).
6. The admin interface should display all fields of the models.
7. Middleware must be implemented to block requests from blacklisted IP addresses.
8. A periodic task must be created to send notifications daily to employees who have not registered for more than 2 days.

## Setup Instructions

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Set up PostgreSQL database and update the configuration in `settings.py`.
4. Run migrations with `python manage.py migrate`.
5. Create a superuser with `python manage.py createsuperuser`.
6. Start the server with `python manage.py runserver`.

## API Documentation

Access the API documentation via the Swagger UI at `/swagger/`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
