import sys
import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, Any

def load_api_key() -> Optional[str]:
    load_dotenv()
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if not api_key:
        print("Ошибка: API ключ не найден. Создайте файл .env с переменной OPENWEATHER_API_KEY")
        return None

    return api_key


def get_weather(city_name: str, api_key: str) -> Optional[Dict[str, Any]]:
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("Ошибка: Неверный API ключ. Проверьте OPENWEATHER_API_KEY в файле .env")
            return None
        elif response.status_code == 404:
            print(f"Город '{city_name}' не найден. Проверьте название и попробуйте снова.")
            return None
        else:
            print(f"Ошибка API: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.Timeout:
        print("Ошибка: Превышено время ожидания ответа от сервера. Попробуйте позже.")
        return None
    except requests.exceptions.ConnectionError:
        print("Ошибка: Нет подключения к интернету. Проверьте соединение.")
        return None
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return None


def display_weather(weather_data: Dict[str, Any]) -> None:
    city_name = weather_data.get('name', 'Неизвестно')
    temp = round(weather_data['main']['temp'])
    description = weather_data['weather'][0]['description']

    print('*******')
    print(f"Погода в городе: {city_name}")
    print(f"Температура: {temp}°C")
    print(f"Описание: {description.capitalize()}")
    print('*******')


if len(sys.argv) != 2:
    print("Ошибка: Необходимо указать название города.")
    print("Пример: python weather.py Moscow")
    sys.exit(1)

city_name = sys.argv[1].strip()

if not city_name:
    print("Ошибка: Название города не может быть пустым.")
    sys.exit(1)

api_key = load_api_key()
if not api_key:
    sys.exit(1)

weather_data = get_weather(city_name, api_key)
if not weather_data:
    sys.exit(1)

display_weather(weather_data)