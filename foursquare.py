# ------------ Flask ------------

from flask import request 
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return render_template("hello.html")


@app.route("/<name>/hello/goodbye") 
def hello_someone(name):
	return "Hello {0}!".format(name.title())

@app.route("/signup", methods=['POST'])
def signup ():
	form_data = request.form
	print form_data['name']
	print form_data['email']
	return "ALL OK"

app.run()

# ------------ FourSquare API ------------

import requests

foursquare = raw_input ('Find the best places to eat, drink, shop, or visit in any city in the world.')

req = requests.get("http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=3ab047edc5cab272c4ab34832062c44a".format(city_name=city))

data = req.json()

print "The weather in {city} is {description}".format(city=data['name'],description=data['weather'][0]['description'])



https://api.foursquare.com/v2/venues/search?ll=51.504557,-0.017334
&query=bars&restaurants&hotels&shops=browse&checkin
&client_id=0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2
&client_secret=2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO
&v=20161024


