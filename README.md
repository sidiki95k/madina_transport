Madina Transport Project
Project Description
Madina Transport is a web-based platform designed to manage transportation and logistics for suppliers, products, orders, and shipments. 
It provides an efficient interface for handling customer information, managing orders, and tracking shipments, all using a microservice architecture powered by Docker containers.

The project leverages FastAPI for the backend, PostgreSQL as the database, and SQLAlchemy as the ORM with Alembic for database migrations.
The app is fully containerized using Docker, allowing easy scalability and portability across environments.

Features
Customers Management: APIs to create, read, update, and delete customer information.
Products Management: APIs to manage the product inventory and details.
Order Processing: Handle customer orders, including items and quantities.

Shipments: Track the shipment status and related information.
Suppliers: Manage supplier details and shipment-related information.

Project Setup
Requirements
To run this project, ensure you have the following installed:

Python 3.10 or higher
Docker
Docker Compose
PostgreSQL
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/sidiki95k/madina_transport.git
cd madina_transport
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables: Create a .env file with the following keys:

bash
Copy code
SQLALCHEMY_DATABASE_URL=postgresql://username:password@db/madina_transport
Run database migrations: Alembic is used for handling database migrations:

bash
Copy code
alembic upgrade head
Run the project using Docker:

bash
Copy code
docker-compose up --build
Running Tests
To run tests, use the following command:

bash
Copy code
pytest
API Documentation
The FastAPI framework automatically generates interactive API documentation, which can be accessed by visiting http://localhost:8000/docs after running the application.

Project Structure
/app: Contains all application-specific code such as routers, models, schemas, and CRUD operations.
/alembic: Contains database migration files.
/routers: Contains all the API route definitions for handling categories, customers, order items, orders, products, shipments, and suppliers.
/models: Defines SQLAlchemy models for the database.
/schemas: Contains Pydantic schemas for data validation.
/crud.py: Implements the database operations (Create, Read, Update, Delete).
Dockerfile: Defines the Docker image for the project.
docker-compose.yml: Defines and runs multi-container Docker applications (web and PostgreSQL).

License
This project is licensed under the MIT License.
