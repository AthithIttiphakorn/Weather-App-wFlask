#Flask instance running server session
from flask import Flask, render_template, request
#Get get_current_weather function from weather.py
from weather import get_current_weather
#waitress for deployable server
from waitress import serve


app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather')
def get_weather():
    #get city name from HTML form
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if city == None or not bool(city.strip())  :
        city = "Shenzhen"

    #send city name for API call to retrieve data in other file
    weather_data = get_current_weather(city)

    #city is not found by API
    if weather_data['cod'] != 200:
        return render_template(
            "error.html",
            error="Not a real city! Check for typos ;)",
            )


    else:
        #return data retrieved from API
        return render_template(
            #access file weather.html
            "weather.html",
            error="",
            #this is the {{ title }} var substitution with the name of the city "name" is the dictionary key from the json file that came with the API. So it is being used here.
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            #use different type of quote when doing this, python will get confused.
            temp=f"{weather_data['main']['temp'] - 273.15 :.1f}",
            feels_like=f"{weather_data['main']['feels_like'] - 273.15 :.1f}",
        )
if __name__ == "__main__":
    #add app is first parameter if does not work
    #change to waitress production server using code below
    #serve(app, host="0.0.0.0", port=8000)
    #run using flask's built in development server.
    app.run(debug=True, host="0.0.0.0", port=8000)

#env and venv was not pushed to GitHub to improve security. To make a .venv and a .env  do py 
#-m venv .venv in bash terminal. To get .env to store API keys just make a file '.env' in VSCode.
