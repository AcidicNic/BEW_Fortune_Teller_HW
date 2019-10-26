from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def results():
    fortune = {
        'name': request.args.get('name'),
        'siblings': request.args.get('siblings'),
        'thing': request.args.get('thing')
    }
    return render_template('results.html', fortune=fortune)

if __name__ == '__main__':
    app.run()
