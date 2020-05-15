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

    #<b> </b> This is HTML code for bold

@app.route("/1006")
def home():
    #return"<p> This is my <b>1006</b> website.<p>"
    return render_template("1006.html")

@app.route("/columbia")
def columbia():
    return "Columbia!"

#This is a comment

#start the server
if __name__ == "__main__":
    app.run()
