from flask import Flask, render_template, request

app= Flask(__name__)
import requests
from bs4 import BeautifulSoup
import time
#엑셀쓰기 위한 준비
from openpyxl import Workbook
write_wb = Workbook()
write_ws = write_wb.active

from  selenium import webdriver
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route("/result",methods=['post'])
def result():
    keyword = request.form['input1']
    page= request.form['input2']
    daum_list=[]
    for num in range(1,int(page)+1):
        url = "https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=" + keyword + "&p=" + str(
            num)
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        print(url)
        for i in soup.find_all("a", class_="link_major"):
            print(i.text)
            daum_list.append(i.text)
    for i in range(1,len(daum_list)+1):
        write_ws.cell(i,1,daum_list[i-1])#worksheet의 cell에 추가
    write_wb.save("static/result.xlsx") #workbook에 저장

    return render_template('result.html',daum_list=daum_list)
@app.route("/naver_shopping", methods=['POST'])
def naver_search():
    search= request.form['input3']
    print("여기는 들어와야지 ",search)
    search_list=[]
    search_list_src=[]
    driver= webdriver.Chrome()
    #3초 기다려주기 , 웹페이지 로딩까지
    driver.implicitly_wait(3)
    driver.get("https://search.shopping.naver.com/search/all?query=" + search)
    #스크롤 내리기
    dict1={}
    y=1000
    for timer in range(0,5):
        driver.execute_script("window.scrollTo(0, " +str(y)+")")
        y= y+1000
        time.sleep(1)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    select = "#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx"
    cnt = 0
    for i in soup.select(select)[0].find_all("div", class_="product_item__MDtDF"):
        if i.text is not None:
            dict1['data'+str(cnt)]=[]
            for j in i.text.split(" "):
                if j.strip() !='': #공백이 아닐경우만 추가
                    dict1['data'+str(cnt)].append(j)
        cnt +=1
    driver.close()
    time.sleep(2)
    #빈데이터는 버리고 2차원 리스트로 저장하고 html에서 2중 반복문으로 처리함
    return render_template("shopping.html",
                           data0=dict1['data0'],
                           data1=dict1['data1'],
                           data2=dict1['data2'],
                           data3=dict1['data3'],
                           data4=dict1['data4']
                           )
if __name__=="__main__":
    app.run()