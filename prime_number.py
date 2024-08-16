import streamlit as st

st.image("prime.jpg")
st.title("Checking for Prime Number")

num = st.text_input("Enter any number")
if num.isdigit():
    num = int(num)
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                st.warning("Not a prime number")
                st.select_slider("Rate the program", ["Bad", "Average", "Good", "Excellent", "Outstanding"], key="slider_not_prime")
                st.button("Submit", key="button1")   #used keys for uniqueness
                break
        else:
            st.success("Prime number")
            st.markdown("### Congratulations!!")
            st.select_slider("Rate the program", ["Bad", "Average", "Good", "Excellent", "Outstanding"], key="slider_prime")
            st.button("Submit", key="button2")
            st.balloons()
    else:
        st.error("Enter a number greater than 1")
        st.select_slider("Rate the program", ["Bad", "Average", "Good", "Excellent", "Outstanding"], key="slider_low_num")
        st.button("Submit", key="button3")
else:
    if num:
        st.error("Error: Invalid number")
        st.select_slider("Rate the program", ["Bad", "Average", "Good", "Excellent", "Outstanding"], key="slider_invalid_num")
        st.button("Done", key="button4")

st.sidebar.title("USER INFO:")
st.sidebar.text_input("Enter your name")
st.sidebar.text_input("Enter your email address")
st.sidebar.file_uploader("Drop your image")
st.sidebar.radio("Select your gender", ["Man", "Woman", "Other"])
st.sidebar.button("Submit", key="sidebar_button")





        
