from flask import Flask
from flask import render_template, request

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():
    return (render_template("index.html"))
    # if request.method == "POST":
    #     num = float(request.form.get("rates"))
    #     return(render_template("index.html", result = 90.2-(50.6*num)))
    # else:
    #     return render_template("index.html", result ="Waiting……….")
    
if __name__ == "__main__":
    app.run()
