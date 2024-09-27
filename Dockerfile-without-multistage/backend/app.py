from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    # Collect system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    metrics = {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage
    }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

