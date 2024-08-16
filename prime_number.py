import streamlit as st


st.image("prime.jpg")
st.title("checking for prime number")
num=st.text_input("enter any number")
if num.isdigit():
    num=int(num)
    if num > 1:
        for i in range(2,num):
              if num%i==0:
                 st.warning("not prime number")
                 st.select_slider("Rate the program",["Bad","Average","Good","Excellent","Outstanding"])     
                 st.button("Submit")
                 break
        else:
            st.success("prime number")
            st.markdown("### congratulations!!")
            st.select_slider("Rate the program",["Bad","Average","Good","Excellent","Outstanding"])     
            st.button("Submit")
            st.balloons()
    else:
        st.error("enter a number greater than 1")
        st.select_slider("Rate the program",["Bad","Average","Good","Excellent","Outstanding"])     
        st.button("Submit")        
else:
    if num:
        st.error("error in valid number")
        st.select_slider("Rate the program",["Bad","Average","Good","Excellent","Outstanding"])     
        st.button("Done")  

st.sidebar.title("USER INFO:")
st.sidebar.text_input("Enter your name")
st.sidebar.text_input("Enter your email address")
st.sidebar.file_uploader("Drop your image")
st.sidebar.radio("select the gender",["man","woman","other"])
st.sidebar.button("Submit")





        
