import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Quote Generator", page_icon="💡")

# Title
st.title("💡 Random Quote Generator")

# Sample quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
    "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
]

# Button to generate quote
if st.button("✨ Generate Quote"):
    quote = random.choice(quotes)
    st.success(quote)
else:
    st.info("Click the button to generate a random quote!")

