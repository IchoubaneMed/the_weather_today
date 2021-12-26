from flask.scaffold import _matching_loader_thinks_module_is_package
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        formCity = request.form.get('city')
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=49b7a11ec275d76aa328aec46e8ca817'
        rApi = requests.get(url.format(formCity)).json()
        curWeather = {
            'city': rApi['name'],
            'temperature': "%.2f" % (rApi['main']['temp'] - 273.15),
            'description': rApi['weather'][0]['description'],
            'icon': rApi['weather'][0]['icon'],
            'lon' : rApi['coord']['lon'],
            'lat' : rApi['coord']['lat']
        }
        return render_template('index.html', curWeather=curWeather)
    else:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=49b7a11ec275d76aa328aec46e8ca817'
        city = 'Ottawa'
        rApi = requests.get(url.format(city)).json()
        print(rApi)
        curWeather = {
            'city': rApi['name'],
            'temperature': "%.2f" % (rApi['main']['temp'] - 273.15),
            'description': rApi['weather'][0]['description'],
            'icon': rApi['weather'][0]['icon'],
            'lon' : rApi['coord']['lon'],
            'lat' : rApi['coord']['lat']
        }
        return render_template('index.html', curWeather=curWeather)


if __name__ == "__main__":
  app.run()