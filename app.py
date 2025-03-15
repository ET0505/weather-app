from flask import *
import requests 

app = Flask(__name__)

# API key
app.key = "77c62ab46f506f753e48c6fd6cf5f083"

# Decorator 
@app.route('/', methods = ["GET", "POST"]) 


def index(): 
  weather_data = None
  if request.method == "POST":
    city = request.form.get("city")
    if city:
      url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app.key}&units=metric"

      response = requests.get(url)

      # 200 OK status successful 
      if response.status_code == 200:
        weather_data = response.json()
    
      else:
        weather_data = None
  

  return render_template("index.html", weather_data = weather_data) 


if __name__ == "__main__":
  app.run(debug = True)
