from flask import Flask, render_template, request, jsonify
import requests



app = Flask(__name__, template_folder='.')

API_KEY = '8cf09b9f1afc7c0359c1f92e1ce1a106'

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Istanbul')
    country = request.args.get('country', '') 
    if country:
        location = f"{city},{country}"
    else:
        location = city

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Şehir bulunamadı'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
