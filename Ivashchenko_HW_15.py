import requests

Base_url = 'http://api.openweathermap.org/data/2.5/weather?'
Api_key = 'c0dcf98c9d901302e4db678c3ee3790b'


def weather_output(city_name):
    complete_url = Base_url + "appid=" + Api_key + "&q=" + city_name
    response = requests.get(complete_url)
    if response.status_code != 200:
        msg = 'openweathermap.org returned non-200 code. Actual code is: {code}, message is: {message}'.format(
            code=str(response.status_code),
            message=response.json()['message']
        )
        raise RuntimeError(msg)
    r_data = response.json()
    if r_data["cod"] != "404":
        y = r_data['main']
        current_t = y['temp']
        current_p = y["pressure"]
        return f'Temperature is {str((round(current_t - 273.15)))}, Pressure is {str(current_p)}'
    else:
        print('city not found')


if __name__ == '__main__':
    print(weather_output(input('please fill up your city ')))


# 1. создать функцию(ии) для  определения погоды по данным(Город).
# 2. Вынести некоторрые данные в константу(ы).
# 3. Для запуска функции использовать if __name__ == '__main__': запуск!
# 4. Создать файл test.py  внутри создать Класс для тестирования функции, с помощью unittest.
