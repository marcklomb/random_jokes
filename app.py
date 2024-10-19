import streamlit as st
import random


# title
st.title("Random joke generator ")

# list of joke
jokes = [

    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why are elevator jokes so classic and good? They work on many levels.",
    "Why don’t skeletons fight each other? They don’t have the guts."
]

#button to generate
if st.button("tell me a joke"):
    joke = random.choice(jokes)
    st.write(joke)

else:
    st.write("click the button to hear a joke")