
# CRUD App with Flask, Python, PostgreSQL, React, and Docker

This project is a simple CRUD (Create, Read, Update, Delete) application built with Flask (Python), PostgreSQL, React, and Docker.

## Features

- Create, Read, Update, and Delete operations for a basic entity.
- Backend API built with Flask.
- Frontend user interface built with React.
- Database powered by PostgreSQL.
- Dockerized for easy deployment.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your machine.
- Node.js and npm installed for the React frontend.
- Python and pip installed for the Flask backend.
- A running PostgreSQL server.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ank-its/CRUD-Rest-API.git
    ```

2. Change into the project directory:

    ```bash
    cd CRUD-Rest-API
    ```

3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

## Configuration

Make sure to set up the necessary environment variables for the Flask backend and React frontend. Create `.env` files in the `backend` and `frontend` directories, respectively, based on the provided examples.

### Backend (.env file in backend directory):

```plaintext
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost:5432/test_db

