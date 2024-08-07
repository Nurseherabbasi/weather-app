from flask import Flask, render_template, request, jsonify
import requests
import redis
import json
from datetime import timedelta
from flasgger import Swagger

app = Flask(__name__, template_folder='.')
swagger = Swagger(app)  

API_KEY = '8cf09b9f1afc7c0359c1f92e1ce1a106'


redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Get the current weather for a city.
    ---
    parameters:
      - name: city
        in: query
        type: string
        required: true
        description: Name of the city
      - name: country
        in: query
        type: string
        required: false
        description: Country code (optional)
    responses:
      200:
        description: Weather data
        schema:
          type: object
          properties:
            city:
              type: string
              description: City name
            temperature:
              type: number
              format: float
              description: Temperature in Celsius
            description:
              type: string
              description: Weather description
      500:
        description: Error message
    """
    city = request.args.get('city', 'Istanbul')
    country = request.args.get('country', '') 
    if country:
        location = f"{city},{country}"
    else:
        location = city

    cache_key = f"weather:{city}:{country}"
    
    try:
        
        cached_data = redis_client.get(cache_key)
        if cached_data:
            return jsonify(json.loads(cached_data))
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'weather' in data:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
            
            
            redis_client.setex(cache_key, timedelta(minutes=5), json.dumps(weather_data))
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'Beklenmeyen veri yapısı'}), 500
    except redis.RedisError as e:
        print(f"Redis error: {str(e)}")  
        return jsonify({'error': 'Veri cache işlemi sırasında bir hata oluştu.'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API isteği başarısız: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Bir hata oluştu: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
