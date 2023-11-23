#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class

@app.route("/index")

def second_flask():
    name = "Gargi"
    return render_template("index.html", index_variable = name)

app.run(debug=True)
