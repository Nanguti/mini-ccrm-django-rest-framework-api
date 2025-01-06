# Django Mini-CRM API

## API Overview

This API is designed to handle a mini-CRM system, including operations for leads, contacts, and notes. It follows REST principles and can be tested using the DRF (Django Rest Framework) GUI.

## Base URL

- **Production Base URL:** `https://emmerce.homeschoolafrica.com`

## Endpoints

### Leads

- **Get All Leads:**
  - `GET /api/leads/`
- **Create a Lead:**
  - `POST /api/leads/`
- **Update a Lead:**
  - `PUT /api/leads/1/` (replace `1` with the lead's ID)
- **Delete a Lead:**
  - `DELETE /api/leads/1/` (replace `1` with the lead's ID)
- **View a Specific Lead:**
  - `GET /api/leads/1/` (replace `1` with the lead's ID)

### Contacts

- **Get All Contacts:**
  - `GET /api/contacts/`
- **Create a Contact:**
  - `POST /api/contacts/`
- **Update a Contact:**
  - `PUT /api/contacts/1/` (replace `1` with the contact's ID)
- **Delete a Contact:**
  - `DELETE /api/contacts/1/` (replace `1` with the contact's ID)
- **View a Specific Contact:**
  - `GET /api/contacts/1/` (replace `1` with the contact's ID)

### Notes

- **Get All Notes:**
  - `GET /api/notes/`
- **Create a Note:**
  - `POST /api/notes/`
- **Update a Note:**
  - `PUT /api/notes/1/` (replace `1` with the note's ID)
- **Delete a Note:**
  - `DELETE /api/notes/1/` (replace `1` with the note's ID)
- **View a Specific Note:**
  - `GET /api/notes/1/` (replace `1` with the note's ID)

---

## Setup Instructions

### Prerequisites

- Python 3.11 or later
- Virtual Environment (recommended)

### 1. **Setting Up the Environment**

#### Windows:

1. Install **Python 3.11** or later from [python.org](https://www.python.org/downloads/).
2. Open a terminal/command prompt and create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

#### macOS and Linux:

1. Install **Python 3.11** or later from [python.org](https://www.python.org/downloads/) or using a package manager like Homebrew (macOS):

   ```bash
   brew install python
   ```

2. Open a terminal and create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### 2. **Setting Up the Database**

Ensure you have a database configured and set the appropriate database settings in `settings.py` in the `DATABASES` section. The default configuration assumes SQLite, but you can configure it for PostgreSQL, MySQL, or another database if necessary.

### 3. **Running the Project**

After installing the dependencies, run the following command to start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000`.

---

## Testing the API with DRF GUI

You can test the API using Django Rest Framework's browsable API interface. Once the server is running, navigate to the following URL to interact with the API:

- [DRF Browsable API Interface](http://127.0.0.1:8000)

From there, you can perform CRUD operations on the `leads`, `contacts`, and `notes` resources.

---

## API Response Format

The API returns data in JSON format. Here are examples of responses:

### Success Response (200 OK)

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "status": "active"
}
```

### Error Response (400 Bad Request)

```json
{
  "error": "Invalid data"
}
```
