from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)  # Setup the app
CORS(app)

@app.get("/")  # Get the values in the app by implementing get request
def index_get():
    return render_template("base.html")  # Open and run the HTML file to get the necessary messages


@app.post("/predict")  # The app will start predicting route by calling the function predict by implementing the post request
def predict():
    text = request.get_json().get("message")  # Will receive the message from the Json file
    # TODO: Check if the text is valid

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
