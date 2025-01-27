from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Function to fetch a quote from an API
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return {
                "content": data.get("content"),
                "author": data.get("author")
            }
        else:
            return {"content": "Could not fetch quote.", "author": "Unknown"}
    except Exception as e:
        return {"content": "Error connecting to API.", "author": "Unknown"}

@app.route('/')
def home():
    quote = get_quote()
    return render_template("index.html", quote=quote)

@app.route('/api/quote')
def api_quote():
    quote = get_quote()
    return jsonify(quote)

if __name__ == "__main__":
    app.run(debug=True)
