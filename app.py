import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app

def main():
    


    menu = ['Home','분석']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice =='Home' :
        run_home_app()
    elif choice =='분석' :
        run_eda_app()
    








if __name__ =='__main__' :
    main()