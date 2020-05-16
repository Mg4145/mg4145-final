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

@app.route("/Classes")
def home():
    #return"<p> This is my <b>1006</b> website.<p>"
    return render_template("Classes.html")

@app.route("/Assignments")
def columbia():
    return render_template("Assignments.html")

#start the server
if __name__ == "__main__":
    app.run()
