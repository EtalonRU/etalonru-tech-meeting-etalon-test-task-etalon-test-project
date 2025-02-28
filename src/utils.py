from typing import Optional

from fastapi import requests

from config import settings


async def get_weather(city: str) -> Optional[str, int]:
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/'
        f'weather?q={city}&appid={settings.OPEN_WEATHER_API_KEY}'
    )
    response_data = response.json().get('main')
    return response_data
