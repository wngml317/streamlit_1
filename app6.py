from tkinter.messagebox import NO
import streamlit as st
import pandas as pd

def main() :
    
    # 유저한테 입력을 받는 방법
    
    # 1. 이름 입력 받기
    name = st.text_input('이름 입력하세요!')
    if name != '' :
        st.subheader(name + '님 안녕하세요')


if __name__ == '__main__' :
    print(__name__)
    main()