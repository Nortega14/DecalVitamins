from flask import Flask, jsonify
from flask_cors import CORS
import random

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Sample quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "An obstacle is often a stepping stone.",
    "The journey of a thousand miles begins with a single step."
]

# Route to serve a random quote
@app.route('/api/quote', methods=['GET'])
def get_quote():
    random_quote = random.choice(quotes)
    return jsonify({"quote": random_quote})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

