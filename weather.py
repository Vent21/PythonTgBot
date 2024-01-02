import requests
import datetime

from data.configs import WEATHER_API

ru_months = {1: "Января",
             2: "Февраля",
             3: "Марта",
             4: "Апреля",
             5: "Мая",
             6: "Июня",
             7: "Июля",
             8: "Августа",
             9: "Сентября",
             10: "Октября",
             11: "Ноября",
             12: "Декабря"}


def get_weather():
    try:
        call = requests.get(WEATHER_API)

        data = call.json()
        cur_weather = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        visibility = data["visibility"]
        weather_id = data["weather"][0]["id"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        today = datetime.datetime.now()

        result = (f"Погода в Новочебоксарске на {today.strftime(f'%H:%M %d {ru_months.get(today.month)} %Y г.')} \n" +
                  f"Температура: {cur_weather} °C\n" +
                  f"Ощущается как: {feels_like} °C\n" +
                  f"Влажность: {humidity} %\n" +
                  f"Давление: {round(pressure * 0.750064, 2)} мм рт.ст.\n" +
                  f"Атмосферные явления: {get_weather_id(weather_id)}\n" +
                  f"Дальность видимости: {visibility} м\n" +
                  f"Скорость ветра: {wind} м/с\n" +
                  f"Сила ветра: {wind_power(wind)}\n" +
                  f"Восход солнца: {sunrise_timestamp.strftime('%H:%M:%S')}\n" +
                  f"Закат солнца: {sunset_timestamp.strftime('%H:%M:%S')}\n" +
                  f"Продолжительность дня: {length_of_the_day}\n")

        return result

    # то, что мы всегда получаем
    except Exception as ex:
        print(ex)
        return "Что то пошло не так!"


def wind_power(wind):
    wind_speed = float(wind)

    if 0 <= wind_speed <= 0.5:
        return "штиль, отсутствие ветра"
    elif 0.6 <= wind_speed <= 1.7:
        return "тихий, дым отклоняется от вертикального направления"
    elif 1.8 <= wind_speed <= 3.3:
        return "легкий, движение воздуха можно определить лицом, шелестят листья"
    elif 3.4 <= wind_speed <= 5.2:
        return "слабый, заметно колебание листьев деревьев, развеваются легкие флаги"
    elif 5.3 <= wind_speed <= 7.4:
        return "умеренный, колеблются тонкие ветки, поднимается пыль, клочки бумаги"
    elif 7.5 <= wind_speed <= 9.8:
        return "свежий, колеблются большие ветки, на воде поднимаются волны"
    elif 9.9 <= wind_speed <= 12.4:
        return "сильный, раскачиваются большие ветки, гудят провода"
    elif 12.5 <= wind_speed <= 19.2:
        return "крепкий, качаются стволы небольших деревьев, на водоемах пенятся волны"
    elif 19.3 <= wind_speed <= 23.2:
        return "буря, ломаются ветви, движение человека против ветра затруднено"
    elif 23.3 <= wind_speed <= 26.5:
        return "сильная буря, срываются домовые трубы и черепица с крыши, повреждаются легкие постройки"
    elif 26.6 <= wind_speed <= 30.1:
        return "полная буря, деревья вырываются с корнем, происходят значительные разрушения легких построек"
    else:
        return "---"


def get_weather_id(id):
    weather = "---"
    match id:
        case 200:
            weather = "Гроза с небольшим дождем"
        case 201:
            weather = "Гроза с дождем"
        case 202:
            weather = "Гроза с сильным дождем"
        case 210:
            weather = "Легкая гроза"
        case 211:
            weather = "Гроза"
        case 212:
            weather = "Сильная гроза"
        case 221:
            weather = "Гроза с порывистым ветром"
        case 230:
            weather = "Гроза с легкой моросью"
        case 231:
            weather = "Гроза с моросью"
        case 232:
            weather = "Гроза с сильной моросью"
        # Виды мороси
        case 300:
            weather = "Легкая морось"
        case 301:
            weather = "Морось"
        case 302:
            weather = "Сильная морось"
        case 310:
            weather = "Легкий моросящий дождь"
        case 311:
            weather = "Моросящий дождь"
        case 312:
            weather = "Сильный моросящий дождь"
        case 313:
            weather = "Дождь с моросью"
        case 314:
            weather = "Сильный дождь с моросью"
        case 321:
            weather = "Ливень с моросью"
        # Виды дождя
        case 500:
            weather = "Легкий дождь"
        case 501:
            weather = "Умеренный дождь"
        case 502:
            weather = "Интенсивный дождь"
        case 503:
            weather = "Сильный дождь"
        case 504:
            weather = "Очень сильный дождь"
        case 511:
            weather = "Ледяной дождь"
        case 520:
            weather = "Легкий ливень"
        case 521:
            weather = "Ливень"
        case 522:
            weather = "Сильный ливень"
        case 531:
            weather = "Рваный ливень"
        # Снег
        case 600:
            weather = "Небольшой снег"
        case 601:
            weather = "Снег"
        case 602:
            weather = "Сильный снег"
        case 611:
            weather = "Снег с мелким дождем"
        case 612:
            weather = "Мокрый снег"
        case 615:
            weather = "Легкий дождь со снегом"
        case 616:
            weather = "Снег с дождем"
        case 620:
            weather = "Легкий снегопад"
        case 621:
            weather = "Снегопад"
        case 622:
            weather = "Сильный снегопад"
        # Атмосферные явления
        case 701:
            weather = "Низкий туман"
        case 711:
            weather = "Дымка"
        case 721:
            weather = "Мгла"
        case 731:
            weather = "Пылевые завихрения"
        case 741:
            weather = "Туман"
        case 751:
            weather = "Песок"
        case 761:
            weather = "Пыль"
        case 762:
            weather = "Вулканический пепел"
        case 781:
            weather = "Торнадо"
        # Чистое небо
        case 800:
            weather = "Чистое небо"
        # Облачность
        case 801:
            weather = "Небольшая облачность"
        case 802:
            weather = "Рассеянные облака"
        case 803:
            weather = "Разрозненные облака"
        case 804:
            weather = "Облачность"
        # Экстримальная погода
    return weather
