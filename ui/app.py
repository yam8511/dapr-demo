"""
邏輯層 - Logic Layer
負責呼叫API，或處理邏輯的程序寫這一層

ps. API = Web Service
"""

import streamlit as st
import logic

st.title("Sample Code")


st.write("點擊按鈕，顯示計數")
if st.button("click"):
    st.write(f"{logic.count()}")


st.write("輸入資料，總和")
a = st.number_input("a")
b = st.number_input("b")
if st.button("sum"):
    st.write(f"a + b = {logic.sum(a,b)}")

st.write("上傳圖片，偵測處理")
imgs = st.file_uploader("img", accept_multiple_files=True)
imgs
# [img.name for img in imgs]

if st.button("upload"):
    logic.upload(imgs[0])
