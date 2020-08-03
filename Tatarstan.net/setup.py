from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")

def Home():
	
	return render_template("main.html")

@app.route("/heros")

def Heros():

	return render_template("heros.html")

@app.route("/news")

def News():

	return render_template("news.html")





@app.route("/ÆÖóÞ¢áñ")




def Junk_page():

	return render_template("ÆÖóÞ¢áñ.html")






@app.route("/confirm_city")

def City():

	return render_template("city.html")

@app.route("/weather")

def Weather():

	city = request.args.get('city', None)
	i = random.randint(0,5)
	statelist = ["snow.png","summer.png","clouds.png","intense-rain.png","partly-cloudy-day.png","storm.png"]
	weatherlist = [" ожидаются снежные осадки."," ожидается ясная погода."," ожидается облачная погода."," ожидается сильный ливень"," ожидается переменная облачность."," ожидаются осадки с грозовыми тучами."]
	image = "/static/" + statelist[i]
	state = "В городе " + city + weatherlist[i] 
	return render_template("weather.html", image = image, state = state)


app.run(debug = True)
