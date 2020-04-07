from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    return render_template('index.html', deaths=data['deaths'], cases=data['cases'], recovered=data['recovered'])

if __name__ == "__main__":
    app.run(debug=True)
