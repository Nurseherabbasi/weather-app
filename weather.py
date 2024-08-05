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
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        if 'weather' in data:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'Beklenmeyen veri yapısı'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API isteği başarısız: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Bir hata oluştu: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
