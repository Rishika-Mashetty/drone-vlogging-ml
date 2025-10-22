from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
latest_location = {}

@app.route("/update_location", methods=["POST"])
def update_location():
    global latest_location
    data = request.json
    if data:
        latest_location = {
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "t": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"[{latest_location['t']}] Latitude: {latest_location['lat']}, Longitude: {latest_location['lon']}")
        return jsonify({"status": "received"}), 200
    return jsonify({"status": "no data"}), 400

@app.route("/get_location")
def get_location():
    return jsonify(latest_location)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
