# Intro

A modular FastAPI service for data validation and candidate scoring.

## Features

- **Data Validation:** Uses Pydantic to enforce integer types.
- **Separated Logic:** Core calculations are isolated from API routes.
- **Interactive Docs:** Auto-generated Swagger UI for testing.

## Project Structure

- `main.py`: API entry point and routing.
- `models.py`: Data schemas and validation rules.
- `logic.py`: Pure Python calculation functions.
- `requirements.txt`: Project dependencies.

## Setup

### 1. Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Execution

```bash
uvicorn main:app --reload
```

## API Endpoints

- **GET `/`**: System health check.
- **POST `/calculate`**: Accepts JSON input and returns the sum.
  - Input: `{"num_1": int, "num_2": int}`

## Testing

Access the interactive documentation at: `http://127.0.0.1:8000/docs`
