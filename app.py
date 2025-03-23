from flask import *
import requests 

app = Flask(__name__)

# API keys
WEATHER_API_KEY = "77c62ab46f506f753e48c6fd6cf5f083"
MAPS_API_KEY = "AIzaSyCOw_xZ5tkEm8rmtFQLLM_bScAT85eBZLk"

# Decorator 
@app.route('/', methods = ["GET", "POST"]) 

def index(): 
  weather_data = None

  # Sumbitting data to the server 
  if request.method == "POST":
    city = request.form.get("city")

    # if valid city then retrieve data from url
    if city:
      url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

      response = requests.get(url).json()

      # 200 OK status successful 
      if response.get("cod") == 200:
        weather_data = {
          "latitude": response["coord"]["lat"],
          "longitude": response["coord"]["lon"],
          "temperature": response["main"]["temp"],
          "description": response["weather"][0]["description"],
          "country": response["sys"]["country"],
          "city": response["name"],
          "feels_like": response["main"]["feels_like"],
          "min_temp": response["main"]["temp_min"],
          "max_temp": response["main"]["temp_max"],
        }

        print(response)

      else:
        weather_data = None

      #make a drop down menu for the cities 

  return render_template("index.html", weather_data = weather_data, maps_key = MAPS_API_KEY) 


if __name__ == "__main__":
  app.run(debug = True)
