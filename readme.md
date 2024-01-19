# MindLab API

MindLab API is a FastAPI-based web service for managing analysis records in a MongoDB database.

## Table of Contents

- [Features](#features)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Submit and retrieve analysis records.
- Paginated retrieval of records.
- MongoDB backend for data storage.

## Database Schema

The MongoDB database used by MindLab API has a single collection named `analysis_records`. The schema for each document in this collection follows the structure of the `AnalysisRecord` Pydantic model.

```json
{
  "user_id": "string",
  "tool_id": "string",
  "timestamp": "datetime",
  // Other optional fields such as agent, ip, etc.
}
```

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB server installed and running.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mindlab-api.git
   cd mindlab-api
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file in the project root with the following content:

```dotenv
MONGODB_URL=mongodb://localhost:27017/
```

Replace the `MONGODB_URL` value with your MongoDB server URL.

## Running the API

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000/`.
Also use you url `http://127.0.0.1:8000/docs` endpoint to interact with the api.
## API Endpoints

- **Submit Record:**
  - Endpoint: `POST /records/`
  - Submit a new analysis record.

- **Get Records:**
  - Endpoint: `GET /records/`
  - Retrieve analysis records with optional pagination (query parameters: `skip` and `limit`).

## Testing

To run tests, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

