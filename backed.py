from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple dictionary to simulate a database for storing URLs
url_database = {}

# Function to generate a short URL
def shorten_url(long_url):
    short_code = str(hash(long_url) % 10000)  # Simple hash to generate a 4-digit code
    short_url = f"https://short.ly/{short_code}"
    url_database[short_code] = long_url  # Store in mock database
    return short_url

# Route to shorten URL
@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.json
    long_url = data.get('url')
    
    # Validate if the URL is provided
    if not long_url:
        return jsonify({'error': 'No URL provided'}), 400
    
    # Generate short URL
    short_url = shorten_url(long_url)
    
    return jsonify({'shortUrl': short_url})

# Route to redirect from short URL to long URL (Optional Feature)
@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return f"🔗 Redirecting to: <a href='{long_url}'>{long_url}</a>"
    else:
        return "⚠️ Invalid or expired URL.", 404

if __name__ == '__main__':
    app.run(debug=True)