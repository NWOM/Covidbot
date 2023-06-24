from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Local Rasa server URL
rasa_server_url = 'http://0.0.0.0:5005'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]

    # Send user message to local Rasa server
    rasa_response = requests.post(rasa_server_url, json={"message": user_message})
    rasa_response = rasa_response.json()

    # Extract the response from Rasa server
    bot_response = rasa_response[0]['text']

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
