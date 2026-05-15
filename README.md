# Calculator API with Advanced Testing

A robust, clean, and well-tested Calculator API built with Python and Django Rest Framework.

## Features Nandini

- **Basic Operations**: Addition, Subtraction, Multiplication, Division.
- **Advanced Operations**: Power (Exponentiation), Square Root.
- **Error Handling**: 
  - Prevents division by zero.
  - Handles square roots of negative numbers.
  - Validates input types and missing fields.
- **Comprehensive Testing**: Over 11 unit and integration tests covering standard logic and edge cases.

## Tech Stack

- **Python 3.12+**
- **Django**: Web Framework.
- **Django Rest Framework (DRF)**: API Toolkit.
- **SQLite**: Local Database (for development).

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd calcPython
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

## Usage

### Run the Development Server
```bash
python manage.py runserver
```

### API Endpoint
**URL**: `http://localhost:8000/api/calculate/`  
**Method**: `POST`  
**Payload**:
```json
{
  "operation": "add",
  "a": 10,
  "b": 5
}
```

**Supported Operations**: `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`.

### Running Tests
```bash
python manage.py test calculator
```

## Advanced Testing Details
The project includes:
- **Unit Tests**: Verifying the core logic in `services.py`.
- **Integration Tests**: Ensuring the API endpoint responds correctly with appropriate status codes (200 OK, 400 Bad Request, etc.).
- **Edge Case Testing**: Specifically handling mathematical impossibilities and malformed requests.
