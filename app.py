from flask import Flask, request, jsonify
from flask_cors import CORS
import re  # Import regex module for text cleaning

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Function to clean input (removes special characters & converts to lowercase)
def clean_input(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

@app.route("/", methods=["GET"])
def home():
    return "Bharat Avenue Chatbot is Live! 🚀", 200

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        user_message = clean_input(request.json.get("message", ""))

        responses = {
            "hi": "Hi, welcome to Bharat Avenue! How can I assist you?",
            "hello": "Hello! Welcome to Bharat Avenue. How can I help?",
            "do you offer free wifi": "Yes, we offer free Wi-Fi to all our guests.",
            "what are your checkin timings": "Check-in time is from 12:00 PM onwards.",
            "what are your checkout timings": "Check-out time is until 11:00 AM.",
            "what facilities do you provide": "We offer free Wi-Fi, room service, laundry, airport pickup, and a restaurant.",
            "do you have a restaurant": "Yes, we have an in-house restaurant serving delicious meals.",
            "is parking available": "Yes, we offer free parking for our guests.",
            "do you allow early checkin": "Early check-in is subject to availability and may have additional charges.",
            "is breakfast included": "No, complimentary breakfast is not included with your stay.",
            "do you have conference rooms": "Yes, we have conference rooms available for business meetings and events.",
            "do you offer airport pickup": "Yes, we provide airport pickup services. Please contact us for details.",
            "do you allow pets": "Sorry, pets are not allowed in our hotel.",
        }

        response_text = responses.get(user_message, "Please select your query from below.")  # No "Sorry" message
        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("✅ Starting Bharat Avenue Chatbot...")
    app.run(host="0.0.0.0", port=10000, debug=True)
