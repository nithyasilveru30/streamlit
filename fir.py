import streamlit as st

st.title("topics")
st.header("machine learning")
st.subheader("part1")
st.info("info")
st.warning("warning")
st.success("success")
st.error("error")
st.write(":moon:")
st.write(":family:")
st.text("hello everyone")
st.caption("welcome")
st.checkbox("login")
st.button("click")
st.selectbox("pick course",["ML","cloud","CS"])
st.radio("pick your gender",["male","female","other"])
st.multiselect("pick course",["ML","cloud","CS"])
st.select_slider("rating",["bad","good","excellent"])
st.slider("enter a number",0,100)
st.number_input("enter number")
st.text_input("enter your name")
st.text_area("enter your details")
st.date_input("select date")
st.time_input("select time")
st.file_uploader("drag files/folders")
st.color_picker("color")
st.progress(90)
