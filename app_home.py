import streamlit as st


def run_home_app() : 
    st.title('유튜브 태그, 타이틀이 조회수에 미치는 영향')
    st.info('환영합니다.')
    st.info('이 앱은 유튜브 트렌디 데이터셋으로 태그, 타이틀, 올린날짜, 올린시간 등이 조회수에 미치는 영향에 대한 내용입니다. ')
    img_url = 'https://blog.kakaocdn.net/dn/bAT9mk/btrPa4mSWwk/kRaA8nIkckdkcHc1amUNOK/img.png'
    st.image(img_url)