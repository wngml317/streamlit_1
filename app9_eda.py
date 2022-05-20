import streamlit as st
import pandas as pd

def run_eda() :
    st.subheader('EDA 화면')
    df = pd.read_csv('data2/iris.csv')

    # 컬럼 이름을 보여주고 
    # 여러 컬럼들 선택 가능하도록 하여
    # 선택한 컬럼들만 화면에 보여줍니다.
    colum_list = st.multiselect('컬럼을 선택하세요', df.columns)
    if len(colum_list) != 0 :
        st.dataframe(df[colum_list])

    # 상관계수를 구하여 화면에 보여줍니다.
    if colum_list != [] :
        st.write('상관계수')
        st.dataframe(df[colum_list].corr())