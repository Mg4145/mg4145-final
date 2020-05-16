############################
# Mauricio Guerrero - mg4145
############################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/Classes")
def home():
    return render_template("Classes.html")

@app.route("/Linux")
def columbia():
    return render_template("Linux.html")

#start the server
if __name__ == "__main__":
    app.run()
