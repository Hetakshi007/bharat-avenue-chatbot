from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Home Route to Confirm App is Running
@app.route("/", methods=["GET"])
def home():
    return "Bharat Avenue Chatbot is Live! 🚀", 200

# ✅ Chatbot Route (Handles Both POST & GET Requests)
@app.route("/chatbot", methods=["POST", "GET"])
def chatbot():
    if request.method == "POST":
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
    
    else:
        return jsonify({"message": "Please use a POST request to interact with the chatbot."}), 200

if __name__ == "__main__":
    print("✅ Starting Bharat Avenue Chatbot...")
    app.run(host="0.0.0.0", port=10000, debug=True)
