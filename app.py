from flask import Flask

app = FLASK(_name_)

@app.route("/info")
def rohaninfo():
	return "I am Rohan from India"

@app.route("/contact")
def rohancontact():
	return "9172148"

app.run(host="0.0.0.0")
