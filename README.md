<h1>CRM System Management</h1>

A Customer Relationship Management (CRM) project built with Django.

## Features

- **Add Records**: Users can add new records to the database.
- **Update Records**: Users can update existing records.
- **Delete Records**: Users can delete records from the database.
- **User Authentication**:
  - **Login**: Users can log in to the system.
  - **Register**: New users can create an account and log in immediately.

## Prerequisites

- Python (version 3.x)
- Django (version 5.x)
- Virtualenv

## Installation

### 1. Clone the repository

```sh
git clone https://github.com/Mohammed-Aljazzar/CRM-SITE.git
cd CRM-SITE
```

### 2. Set up a virtual environment

#### On Windows

```sh
python -m venv venv
venv\Scripts\activate
```

#### On MacOS/Linux

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required dependencies

```sh
cd src
pip install -r requirement.txt
```

### 4. Apply migrations and start the server

```sh
python manage.py migrate
python manage.py runserver
```

### Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new user account or log in with an existing account.
3. Start adding, updating, and deleting records as needed
