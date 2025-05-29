import streamlit as st
import requests

# Flask API endpoint URL
API_URL = "http://127.0.0.1:5000/shorten"  # Update with your Flask server URL if different

# Streamlit app
st.title("🔗 URL Shortener with Streamlit")
st.write("Enter a long URL below to get a shortened version:")

# Input field for the long URL
long_url = st.text_input("Enter long URL:", placeholder="https://example.com/very/long/url")

# Button to shorten URL
if st.button("Shorten URL"):
    if long_url:
        try:
            # Send request to Flask API
            response = requests.post(API_URL, json={"url": long_url})
            
            if response.status_code == 200:
                # Get shortened URL from response
                short_url = response.json().get('shortUrl')
                st.success(f"✅ Shortened URL: [**{short_url}**]({short_url})")
            else:
                st.error("⚠️ Error shortening URL. Please try again.")
        except Exception as e:
            st.error(f"❌ Unable to connect to the backend: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL before submitting.")