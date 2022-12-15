import streamlit as st


def run_home_app() : 
    st.text('환영합니다.')
    st.text('이 앱은 유튜브 트렌디 데이터에 대한 내용입니다. ')
    img_url = 'https://blog.kakaocdn.net/dn/bAT9mk/btrPa4mSWwk/kRaA8nIkckdkcHc1amUNOK/img.png'
    st.image(img_url)