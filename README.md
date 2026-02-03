# Introduction to Flask

A simple Flask web application demonstrating basic routing and HTTP endpoints.

## Project Structure

```
.
├── hello.py          # Main Flask application
├── README.md         # Project documentation
├── .gitignore        # Git ignore rules
└── __pycache__/      # Python cache directory (auto-generated)
```

## Overview

This is a beginner-friendly Flask project that showcases how to create a basic web server with multiple routes.

## Features

- **Root Route (`/`)**: Returns a simple "Hello, world" greeting
- **Home Route (`/home`)**: Returns a "Welcome home" message

## Installation

1. Clone or navigate to the project directory:
   ```bash
   cd Introduction_to_flask
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install Flask:
   ```bash
   pip install flask
   ```

## Usage

Run the Flask application:

```bash
python hello.py
```

The server will start on `http://localhost:5000` by default.

### Available Routes

- `GET /` - Returns "Hello, world"
- `GET /home` - Returns "Welcome home"

## Dependencies

- Flask

## .gitignore

The project includes a `.gitignore` file to exclude:
- `__pycache__/` - Python cache files
- `*.pyc` - Compiled Python files
- `.venv/` - Virtual environment directory

