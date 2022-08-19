from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.route("/DigitalCard.html")
def cards_get():
    return render_template("DigitalCard.html")

@app.route("/flappyBird.html")
def flappyBird_get():
    return render_template("flappyBird.html")

@app.route("/cv.html")
def cv_get():
    return render_template("cv.html")

@app.route("/certificate.html")
def certificate_get():
    return render_template("certificate.html")

@app.route("/contact.html")
def contact_get():
    return render_template("contact.html")

@app.route("/projectList.html")
def projectList_get():
    return render_template("projectList.html")

@app.route("/clock.html")
def clock_get():
    return render_template("clock.html")

@app.route("/P1Menu.html")
def P1Menu_get():
    return render_template("P1Menu.html")

@app.route("/base.html")
def base_get():
    return render_template("base.html")

@app.route("/alarm.html")
def alarm_get():
    return render_template("alarm.html")

@app.route("/stopwatch.html")
def stopwatch_get():
    return render_template("stopwatch.html")

@app.route("/tictactoe.html")
def tictactoe_get():
    return render_template("tictactoe.html")

@app.route("/racing.html")
def racing_get():
    return render_template("racing.html")

@app.route("/PowerPoint.html")
def PowerPoint_get():
    return render_template("PowerPoint.html")

@app.route("/puzzle.html")
def puzzle_get():
    return render_template("puzzle.html")

@app.route("/ToDo.html")
def ToDo_get():
    return render_template("ToDo.html")

@app.route("/snakegame.html")
def snakegame_get():
    return render_template("snakegame.html")

@app.route("/fighting.html")
def fighting_get():
    return render_template("fighting.html")

@app.route("/memory.html")
def memory_get():
    return render_template("memory.html")

@app.route("/calculator.html")
def calculator_get():
    return render_template("calculator.html")

@app.route("/unit.html")
def unit_get():
    return render_template("unit.html")

@app.route("/currency.html")
def currency_get():
    return render_template("currency.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    #TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
    
if __name__ == "__main__":
    app.run(debug=True)

