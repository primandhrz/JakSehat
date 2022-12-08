from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("./chatbot.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@app.route("/")
def home():
    return render_template("./chatbot.html")

@app.route("/rs")
def rs():
    return render_template("./rs_dki.html")

@app.route("/rs_jakbar")
def rs_jakbar():
    return render_template("./rs_jakbar.html")

@app.route("/rs_jakpus")
def rs_jakpus():
    return render_template("./rs_jakpus.html")

@app.route("/rs_jaksel")
def rs_jaksel():
    return render_template("./rs_jaksel.html")

@app.route("/rs_jaktim")
def rs_jaktim():
    return render_template("./rs_jaktim.html")

@app.route("/rs_jakut")
def rs_jakut():
    return render_template("./rs_jakut.html")

if __name__ == "__main__":
    app.run(debug=True)
