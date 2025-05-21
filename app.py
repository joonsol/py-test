import streamlit as st

st.title("Strealit Test")

name =st.text_input("이름을 입력하세요")

if st.button("확인"):
    st.success(f"{name}님 안녕하세요!")