from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json
    input_text = data.get("input_text", "")
    genai.configure(api_key="api_key")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_text)
    output_text = response.text
    return jsonify({"output_text": output_text})

if __name__ == '__main__':
    app.run(debug=True)
