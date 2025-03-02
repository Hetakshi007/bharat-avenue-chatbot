from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bharat Avenue Chatbot is Live!", 200

@app.route("/chatbot", methods=["POST"])
def chatbot():
    print(f"Received request: {request.json}")  # Debugging log

    user_message = request.json.get("message", "").lower()

    responses = {
        "hi": "Hi, welcome to Bharat Avenue! How can I assist you?",
        "hello": "Hello! Welcome to Bharat Avenue. How can I help?",
        "do you offer free wifi?": "Yes, we offer free Wi-Fi to all our guests.",
        "what are your check-in timings?": "Check-in time is from 12:00 PM onwards.",
        "what are your check-out timings?": "Check-out time is until 11:00 AM.",
        "fallback": "Sorry, I don't understand. Please select a query from the FAQ buttons."
    }

    response_text = responses.get(user_message, responses["fallback"])
    return jsonify({"response": response_text})

if __name__ == "__main__":
    print("Starting Flask app...")  # Extra log to confirm app startup
    app.run(host="0.0.0.0", port=10000, debug=True)
