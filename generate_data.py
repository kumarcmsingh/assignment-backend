from datetime import datetime, timedelta
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from config import token, host as url, org, bucket

# InfluxDB connection details
url = url  # Replace with your InfluxDB URL
token = token  # Replace with your InfluxDB token
org = org  # Replace with your InfluxDB organization
bucket = bucket  # Replace with your InfluxDB bucket

# Number of data points to insert
num_points = 5000

# Generate the data points
data_points = []
start_time = datetime.utcnow()

for i in range(num_points):
    value = i + 1  # Example value
    timestamp = start_time + timedelta(seconds=i * 5)
    
    point = Point("o2_reading") \
        .tag("sensor_name", "o2") \
        .tag("sensor_id", 1) \
        .tag("data_type_of_sensor", "univariate") \
        .tag("subsensor", "o2") \
        .field("value", value) \
        .field("units", "ppm") \
        .time(timestamp)
    
    data_points.append(point)

# Initialize InfluxDB client
client = InfluxDBClient(url=url, token=token)

# Create the InfluxDB write API
write_api = client.write_api(write_options=SYNCHRONOUS)

# Batch and write the data points to InfluxDB
batch_size = 10
num_batches = num_points // batch_size

for i in range(num_batches):
    batch_start = i * batch_size
    batch_end = batch_start + batch_size
    batch = data_points[batch_start:batch_end]
    
    write_api.write(bucket=bucket, org=org, record=batch)

# Close the InfluxDB client
client.close()
