from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Chatbot API!"

if __name__ == '__main__':
    app.run(debug=True)

# Import necessary functions from your script
from pdf_query import your_function

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message")
    # Call the function from your script
    response = chat_with_model(user_input)
    return jsonify({"response": response})
