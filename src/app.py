from flask import Flask, jsonify
from whitenoise import WhiteNoise
import json
from oanda_api import OandaAPI
# from kafka import KafkaProducer

# #Prometheus Integration for Monitoring
# from prometheus_client import start_http_server, Summary, Counter, generate_latest

# REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
# REQUEST_COUNT = Counter('request_count', 'Total request count')


app = Flask(__name__)
app.wsgi_app = WhiteNoise(
    app.wsgi_app, root="static/", index_file=True, autorefresh=True
)

# @app.before_request
# def before_request():
#     REQUEST_COUNT.inc()

# @app.route("/metrics")
# def metrics():
#     return generate_latest()

@app.route("/kpi_data")
# @REQUEST_TIME.time()
def get_kpi_data():
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
        return data


# KAFKA Setup
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# def send_message(topic, message):
#     producer.send(topic, message)
#     producer.flush()

@app.route("/price_data/<pair>")
# @REQUEST_TIME.time()
def get_price_data(pair):
    data = OandaAPI.pricing_api(pair)
    # send_message('price_data_topic', data)
    return jsonify(data)

if __name__ == "__main__":
    # start_http_server(9001)
    app.run()