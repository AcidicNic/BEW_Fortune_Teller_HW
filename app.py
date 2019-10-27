from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fortune', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run()
