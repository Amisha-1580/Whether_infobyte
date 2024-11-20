from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample weather data (mocked)
weather_data = {
    "New York": {"temperature": "10°C", "condition": "Cloudy"},
    "London": {"temperature": "8°C", "condition": "Rainy"},
    "Mumbai": {"temperature": "28°C", "condition": "Sunny"}
}

@app.route('/')
def home():
    return render_template('whether.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')  # Retrieve the city name from the form
    if city:
        weather = weather_data.get(city, None)
        if weather:
            return jsonify({"status": "success", "data": weather})
        return jsonify({"status": "error", "message": "City not found"}), 404
    return jsonify({"status": "error", "message": "City not specified"}), 400

if __name__ == '__main__':
    app.run(debug=True)