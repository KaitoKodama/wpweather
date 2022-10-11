import datetime
from weather import WeatherSet
from wordpress import WordPressAuto


wp_auto = WordPressAuto()
dt_now = datetime.datetime.now()
time_stamp = f'{dt_now.year}/{dt_now.month}/{dt_now.day}'

weather_list: list = [
    WeatherSet(label="札幌競馬場", category="sapporo", place="Sapporo"),
    WeatherSet(label="函館競馬場", category="hakodate", place="Hakodate"),
    WeatherSet(label="福島競馬場", category="hukusima", place="Hobaramachi"),
]

for index, item in enumerate(weather_list):
    temp = item.request()
    title = f"{item.label}：{time_stamp}"
    category = item.category
    weather = temp["weather"][0]["description"]
    wp_auto.wp_auto_post(title=title, content=weather, category=category)
