import streamlit as st
import pandas as pd

data = pd.read_csv("2022서울시미세먼지.csv")

st.title('때는 바야흐로2022년도의 마지막 날! 코로나시기 서울특별시의 미세먼지는 어땠을까?')

st.text("'주된 먼지= 미세먼지의 양 - 초미세먼지의 양 < 0인 경우 초미세먼지, 그렇지 않은 경우 미세먼지'로 표기하였습니다.")




color = {'초미세먼지':'#ff0000', '미세먼지':'#ffd700'}
data.loc[:,'color'] = data.copy().loc[:,'주된먼지'].map(color)




data.loc[:,'size'] = 10*(data['미세먼지']+data['초미세먼지'])
data




with st.form("input"):
       date = st.multiselect("시간을 선택하세요.", data['일시'].unique())
       submitted = st.form_submit_button("조회")

if submitted:
    # 'date'에서 사용자가 선택한 값으로 데이터를 필터링
    filtered_data = data[data["일시"].isin(date)]
    
    # 필터링된 데이터가 있는 경우 반복
    if not filtered_data.empty:
       st.map(filtered_data, latitude="위도", longitude="경도", size="size", color="color")
       
    else:
        st.write("선택한 일시에 대한 데이터가 없습니다.")