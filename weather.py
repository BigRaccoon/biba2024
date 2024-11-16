import requests
import json
from datetime import datetime


def act_temperature():
    api_token = '6e91bd80e5a9339f601286e9b72604ed'
    api_token_hours = 'f6de4ddcd6e94e5fb7981301230410'
    city = 'Нижний Новгород'
    url_actual = 'https://api.openweathermap.org/data/2.5/weather?q='+city + \
        '&units=metric&lang=ru&appid=' + api_token
    url = 'http://api.weatherapi.com/v1/forecast.json?key=f6de4ddcd6e94e5fb7981301230410&lang=ru&q=Nizhny Novgorod&days=1&aqi=no&alerts=no'
    weather_data = requests.get(url).json()


# Работаем со временем, чтобы сделать почасовой прогноз
    time_now = datetime.now().hour
    weather_hours_data = weather_data['forecast']['forecastday']
    weather_hours = weather_hours_data[0]['hour']
    reading = json.dumps(weather_hours, indent=2)

# Создаем список из данных о погоде
    temp_for_in_hours = []
    for i in weather_hours:
        str_time = datetime.strptime(i['time'], '%Y-%m-%d %H:%M').hour
        if str_time >= time_now:
            # делает эмодзи погоды
            match i['condition']['code']:
                case 1000:
                    i['condition']['code'] = '☀️'
                case 1003:
                    i['condition']['code'] = '⛅'
                case 1006:
                    i['condition']['code'] = '☁️'
                case 1009:
                    i['condition']['code'] = '☁︎'
                case 1030:
                    i['condition']['code'] = '🌫️'
                case 1063:
                    i['condition']['code'] = '🌦'
                case 1066:
                    i['condition']['code'] = '🌨️'
                case 1069:
                    i['condition']['code'] = '❄️'
                case 1072:
                    i['condition']['code'] = '🥶'
                case 1087:
                    i['condition']['code'] = '⚡'
                case 1114:
                    i['condition']['code'] = '❄'
                case 1117:
                    i['condition']['code'] = '❄️❄️❄️'
                case 1135:
                    i['condition']['code'] = '🌫️🌫️🌫️'
                case 1147:
                    i['condition']['code'] = '❄️🌫️❄️'
                case 1150:
                    i['condition']['code'] = '🌨️'
                case 1168:
                    i['condition']['code'] = '🌨️'
                case 1171:
                    i['condition']['code'] = '🌨️🌨️🌨️'
                case 1180:
                    i['condition']['code'] = '🌦'
                case 1183:
                    i['condition']['code'] = '🌨️'
                case 1186:
                    i['condition']['code'] = '🌧️🌧️'
                case 1189:
                    i['condition']['code'] = '🌧️🌧️🌧️'
                case 1192:
                    i['condition']['code'] = '🌧🌧🌧'
                case 1195:
                    i['condition']['code'] = '🌧🌧🌧'
                case 1198:
                    i['condition']['code'] = '⛆'
                case 1201:
                    i['condition']['code'] = '⛆⛆⛆'
                case 1204:
                    i['condition']['code'] = '❄'
                case 1207:
                    i['condition']['code'] = '❄❄❄'
                case 1210:
                    i['condition']['code'] = '❄'
                case 1216:
                    i['condition']['code'] = '❄'
                case 1219:
                    i['condition']['code'] = '❄'
                case 1222:
                    i['condition']['code'] = '❄❄❄'
                case 1225:
                    i['condition']['code'] = '❄️❄️❄️'
                case 1237:
                    i['condition']['code'] = '🧊'
                case 1240:
                    i['condition']['code'] = '🌧️'
                case 1243:
                    i['condition']['code'] = '🌧️🌧️'
                case 1246:
                    i['condition']['code'] = '🌧️🌧️🌧️🌧️'
                case 1249:
                    i['condition']['code'] = '🌧️️🌧️❄'
                case 1252:
                    i['condition']['code'] = '⋆꙳•❅*‧ ‧*❆ ₊⋆'
                case 1255:
                    i['condition']['code'] = '❅*‧ ‧*❆'
                case 1258:
                    i['condition']['code'] = '*❆*❆*❆*❆*'
                case 1261:
                    i['condition']['code'] = '*❆🧊*❆*🧊❆*🧊❆*'
                case 1264:
                    i['condition']['code'] = '🧊🧊🧊'
                case 1273:
                    i['condition']['code'] = '🌧️⚡️'
                case 1276:
                    i['condition']['code'] = '🌧⚡⚡️🌧⚡⚡⚡⚡⚡⚡⚡️️🌧️'
                case 1279:
                    i['condition']['code'] = '❄️⚡️❄️'
                case 1282:
                    i['condition']['code'] = '❄️⚡️❄️⚡️'
                case _:
                    i['condition']['code'] = 'Смайлик потерялся в iнтернет'

            temp_for_in_hours.append(
                [str_time, round(i['temp_c']), i['condition']['text'], i['condition']['code']])

# Создаем переменную, в которой будут почасовые данные
    hour_temp_for_return = ' Далее нас ожидает:\n'

    if len(temp_for_in_hours) >= 5:
        temp_for_in_hours = temp_for_in_hours[1:6]
        for i in temp_for_in_hours:
            hour_temp_for_return += f'В {i[0]}:00 {i[1]}°C, {i[2]} {i[3]}\n'

    else:
        for i in temp_for_in_hours:
            hour_temp_for_return += f'В {i[0]}:00 {i[1]}°C, {i[2]} {i[3]}\n'

# актуальная температура
    weather_data_actual = requests.get(url_actual).json()
    temperature = round(weather_data_actual['main']['temp'])
    temperature_feels = round(weather_data_actual['main']['feels_like'])
    descrip_weather = weather_data_actual['weather'][0]['description']

# заключаем в переменную текст, содержащий данные о погоде.
    if temperature == temperature_feels:
        temperature = f'Сейчас у нас {temperature} °C, {descrip_weather}.' + \
            hour_temp_for_return
    else:
        temperature = f'Сейчас у нас {temperature} °C, но ощущается как {temperature_feels} °C, {descrip_weather}.' + hour_temp_for_return
    return temperature


act_temperature()
