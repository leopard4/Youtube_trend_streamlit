import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app

def main():
    st.title('유튜브 트렌드 분석')


    menu = ['Home','EDA']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice =='Home' :
        run_home_app()
    elif choice =='EDA' :
        run_eda_app()
    








if __name__ =='__main__' :
    main()