import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

def run_eda_app() : 
    st.title("분석")
    df= pd.read_csv('data/youtube_trend.csv')

    column_list = df.columns
    if st.checkbox('데이터프레임 3개만보기') : 
        st.dataframe(df.head(3))
        st.text('168554 rows × 16 columns')
    if st.checkbox('카테고리별 총개수') :
        st.dataframe(df['categori_name'].value_counts().to_frame())  
    if st.checkbox('특정컬럼만 확인(10개 제한)'):
        selected_column = st.multiselect("",column_list)
        if len(selected_column) >= 1 :
            st.dataframe(df.loc[:, selected_column].head(10))
    
    if st.checkbox("컬럼의정보를 알려줘"):
        category_list = ['title : 제목',
 'publishedAt : 올린날짜',
 'channelTitle : 채널이름',
 'categoryId : 카테고리',
 'tags : 태그',
 'view_count : 조회수',
 'likes : 좋아요',
 'dislikes : 싫어요',
 'comment_count : 댓글수',
 'description : 상세내용작성여부',
 'tag_cnt : 태그수',
 'categori_name : 카테고리이름',
 'time_only : 올린시간',
 'week_day : 숫자요일',
 'title_len : 제목의길이',
 'week_day_name : 글자요일']


        st.table(category_list)
    
  

    if st.checkbox('상관관계분석') :
        column_list2 = ['likes','dislikes','comment_count','tag_cnt','time_only','title_len','week_day','view_count']
        selected_list = st.multiselect('좋아요,싫어요,댓글,태그수,올린시간,제목의길이,올린요일,조회수 순서로 세팅되어있습니다.', column_list2,default=column_list2)
        st.text('필요없는 컬럼은 제거하세요')

        if len(selected_list) > 1 :

            df_corr = df[ selected_list ].corr()

            fig2 = plt.figure()
            sb.heatmap( data= df_corr, annot=True, fmt='.2f', cmap='coolwarm', 
                        vmin= -1, vmax=1, linewidths=0.5)
            st.pyplot(fig2)

            st.info("상관분석결과 : 조회수와 아무런 관련이 없다는것을 알수있다. ")
            st.info("특이한것은 태그의 갯수가 많을수록 타이틀도 길게짓는 경향이 있는것으로 발견되었다.")
            

    # 태그 문자열로 이루어진 리스트 피클을 로드.
    with open("data/list.pickle", "rb") as f:
        flattened_list = pickle.load(f)
    
    search = st.sidebar.text_input("키워드를 검색해보세요.")

    if len(search) >= 1 :
        st.sidebar.info(f"{search}가 태그로 사용된 갯수는 총 "+str(flattened_list.count(search))+"개 입니다.")
        # 평균 조회수를 보여주자.
        
        st.sidebar.info(f"{search}가 태그로 사용된 영상들의 평균 조회수는 "+"{:.0f}".format(df[df['tags'].str.contains(search)]['view_count'].mean())+"입니다.")
    
    # 많이사용된 키워드 10개를 보여주자.
    st.sidebar.subheader("많이 사용된 키워드 10개")
    st.sidebar.text("None은 태그가 없는 영상입니다.")
    st.sidebar.table(pd.Series(flattened_list).value_counts().head(10))
        