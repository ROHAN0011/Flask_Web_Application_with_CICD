from flask import Flask

app = Flask(__name__)

@app.route("/info")
def rohaninfo():
	return "I am Rohan from India"

@app.route("/contact")
def rohancontact():
	return "112372972"

app.run(host="0.0.0.0")