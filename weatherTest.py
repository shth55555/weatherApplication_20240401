import requests  #pip install requests

from bs4 import BeautifulSoup #pip install beautifulsoup4

inputArea = input("날씨를 조회하려는 지역을 입력하세요:")

weatherHtml = requests.get(f"https://search.naver.com/search.naver?&query={inputArea}날씨")
# 네이버에서 한남동 날씨로 검색한 결과 html 파일 가져오기

# print(weatherHtml.text)

weatherSoup =BeautifulSoup(weatherHtml.text,"html.parser")
# print(weatherSoup)

areaText = weatherSoup.find("h2", {"class":"title"}).text  # 날씨 지역 이름 가져오기
areaText = areaText.strip()  # 양쪽 공백 제거
print(f"지역이름 : {areaText}")


todayTempText = weatherSoup.find("div",{"class":"temperature_text"}).text
todayTempText = todayTempText[6:12].strip()  # 6번째 글자부터 슬라이싱 후 양쪽 공백 제거
print(f"현재온도 : {todayTempText}")


yesterdayTempText = weatherSoup.find("span", "temperature up").text
yesterdayTempText = yesterdayTempText.strip()
print(f"어제날씨비교 : {yesterdayTempText}")





todayTempText = weatherSoup.find("span", {"class":"weather before_slash"}).text
todayTempText = todayTempText.strip()
print(f"오늘 날씨 : {todayTempText}")


senseTempText = weatherSoup.find("dd", {"class":"desc"}).text #현재 체감온도
senseTempText = senseTempText.strip()
print(f"체감온도 : {senseTempText}")

todayInfoText = weatherSoup.select("ul.today_chart_list>li")  #미세먼지, 초미세먼지, 자외선, 일몰
# print(todayInfoText)
# print("-----------------------------")
# print(todayInfoText[0])
dustInfo = todayInfoText[0].find("span", {"class":"txt"}).text
dustInfo = dustInfo.strip()
print(f"미세먼지 :{dustInfo}")   #미세먼지 정보

dustInfo2 = todayInfoText[1].find("span",{"class":"txt"}).text
dustInfo2 = dustInfo2.strip()
print(f"초미세먼지 : {dustInfo2}")    #초미세먼지 정보


