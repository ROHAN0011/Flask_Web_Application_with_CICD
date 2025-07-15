from flask import FLASK

app = FLASK(_name_)

@app.route("/info")
def rohaninfo():
	return "I am Rohan from India"

@app.route("/contact")
def rohancontact():
	return "404"

app.run(host="0.0.0.0")
