import streamlit as st
import requests

# Your Instagram credentials
INSTAGRAM_CLIENT_ID = "861261932880977"
REDIRECT_URI = "https://owlit-bot-sandeeps-projects-649f48ac.vercel.app/instagram_redirect"

# Button to start the Instagram login flow
st.title('Instagram Business Login')

# Display the button
if st.button('Login with Instagram'):
    # Generate the Instagram OAuth URL
    authorization_url = (
        "https://www.facebook.com/v13.0/dialog/oauth"
        f"?client_id={INSTAGRAM_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=instagram_basic,pages_show_list"
        "&response_type=code"
    )

    # Redirect to Instagram login
    st.write("Click the button below to log in with Instagram.")
    st.markdown(f"[Login with Instagram]({authorization_url})")
