# Погода в командной строке

Python скрипт для получения текущей погоды по названию города.

## Требования

- Python 3.12 или выше
- Бесплатный API ключ OpenWeatherMap

## Как получить API ключ OpenWeatherMap

1. **Зарегистрироваться** на [OpenWeatherMap](https://openweathermap.org/api)
2. **Подтвердить email**
3. **Найти API ключ** в личном кабинете -> "API Keys"
4. **Скопировать ключ**

## Установка

1. **Клонировать репозиторий**
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

2. **Создать виртуальное окружение**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Установить зависимости**
```bash
pip install -r requirements.txt
```

4. **Настроить API ключ**
- получите API ключ
- cкопируйте файл .env.example в .env
```bash
cp .env.example .env
```
- отредактируйте .env и вставьте ваш API ключ:
```bash
OPENWEATHER_API_KEY=ваш_реальный_ключ
```

## Использование
```bash
python weather.py <название_города>
```