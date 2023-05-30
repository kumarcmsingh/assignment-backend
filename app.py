from flask import Flask, jsonify, request
from influxdb_client import InfluxDBClient
from flask_cors import CORS
from config import token, org, bucket
app = Flask(__name__)
CORS(app)

token = token  # Replace with your InfluxDB token
org = org  # Replace with your InfluxDB organization
bucket = bucket  # Replace with your InfluxDB bucket

client = InfluxDBClient(url="http://localhost:8086", token=token)

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        offset = (page - 1) * per_page

        query = f'from(bucket: "{bucket}") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "o2_reading") |> limit(n: {per_page}, offset: {offset})'
        tables = client.query_api().query(org=org, query=query)
        data = []
        for table in tables:
            for record in table.records:
                data.append(record.values)
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({"status": False})

if __name__ == '__main__':
    app.run(debug=True)

