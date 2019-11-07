from flask import Flask, render_template, request
from random import randint
import requests

app = Flask(__name__)
API_KEY='624946fa3740e42ae61063db4b77c9d6'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fortune', methods=['GET'])
def fortune():
    return render_template('fortune_form.html')


@app.route('/fortune_results')
def results():
    name = request.args.get('name')
    color = request.args.get('color')
    hyd = request.args.get('hyd')
    planet = request.args.get('planet')
    if int(hyd) > 3:
        prediction = "fantastic"
    elif int(hyd) < 3:
        prediction = "bad"
    else:
        prediction = "alright"

    rand_color = "%06x" % randint(0, 0xFFFFFF)
    lucky_number = randint(100000, 999999)

    fortune = {
        'name': name,
        'color': color,
        'rand_color': rand_color,
        'planet': planet,
        'prediction': prediction,
        'lucky_number': lucky_number
    }

    return render_template('results.html', fortune=fortune)


@app.route('/weather')
def weather():
    return render_template('weather_form.html')


@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')
    params = {
        'appid': API_KEY,
        'q': users_city,
        'units': 'Imperial'
    }
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params)
    if not r.status_code == 200:
        print("error")
        return render_template('weather_form.html')
    results = r.json()
    city = results['name']
    degrees = results['main']['temp']
    return render_template('weather_results.html', city=city, degrees=degrees)


if __name__ == '__main__':
    app.run()
