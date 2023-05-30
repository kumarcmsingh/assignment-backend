# Flask API for InfluxDB Data Retrieval

This Flask API allows you to retrieve time-series data from an InfluxDB database. It supports pagination to fetch data in chunks and provides an endpoint to fetch the data as JSON.

## Prerequisites

Before running the API, make sure you have the following dependencies installed:

- Python 3
- Flask
- InfluxDB Python Client
- Flask-CORS

## Configuration

In order to use the API, you need to configure the following variables:

- `token`: Replace with your InfluxDB token
- `org`: Replace with your InfluxDB organization
- `bucket`: Replace with your InfluxDB bucket

Make sure to update these variables in the code before running the API.

## API Endpoints

### GET /api/data

This endpoint retrieves time-series data from the InfluxDB database.

#### Query Parameters

- `page` (optional, default=1): The page number for pagination.
- `per_page` (optional, default=10): The number of records per page.

#### Response

The API responds with JSON data containing the retrieved time-series data.

#### Example Usage

Retrieve the first 10 records:

Retrieve records from the second page with 10 records per page:

Retrieve records from the second page with 20 records per page:

## Usage

1. Install the required Python packages:

2. Configure the `token`, `org`, and `bucket` variables in the code.

3. Run the Flask server:

The API will be accessible at `http://localhost:5000/api/data`.
