from flask import Flask, render_template
import  pandas as pd
import json
import plotly
import plotly.express as px
import MySQLdb

db= MySQLdb.connect(host='localhost',user='root',password='1234', db='izen')
cur = db.cursor()
#sql = "insert into tbl_plot(name,age,city,country) values (%s,%s,%s,%s,%s,%s)"



app=Flask(__name__)

@app.route('/')
def bar_with_plotly():
    # Students data available in a list of list
    # students = [['아카시', 34, '시드니', '호주'],
    #             ['Rithika', 30, '코임바토르', '인도'],
    #             ['Priya', 31, '코임바토르', '인도'],
    #             ['Sandy', 32, '도쿄', '일본'],
    #             ['Praneeth', 16, '뉴욕', '미국'],
    #             ['Praveen', 17, '토론토', '캐나다']]
    sql = "select * from tbl_plot";
    cur.execute(sql)
    datas = cur.fetchall();
    for i in datas:
        print(i)
    df=pd.DataFrame(datas, columns=['pno','Name','Age','City','Country'],index=['a','b','c','d','e','f','g'])
    #bar chart생성
    fig = px.bar(df,x='Name',y='Age',color='City',barmode='group')

    #graphjson 생성
    graphjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('bar.html',grapJson=graphjson)
if __name__ == '__main__':
    app.run(debug=True)