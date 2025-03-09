import streamlit as st
import random

# Function to generate a random number
def generate_number():
    return random.randint(1, 10)

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = generate_number()
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'message' not in st.session_state:
    st.session_state.message = ""

st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 10!")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

# Submit button
if st.button("Submit Guess"):
    if guess:  # Ensure guess is valid
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.session_state.message = "Try a higher number! ⬆️"
        elif guess > st.session_state.number:
            st.session_state.message = "Try a lower number! ⬇️"
        else:
            st.session_state.message = f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!"

# Display message
if st.session_state.message:
    st.write(st.session_state.message)

# Play Again button
if st.button("Play Again"):
    st.session_state.clear()  # Reset everything
    st.rerun()  # Refresh the app


