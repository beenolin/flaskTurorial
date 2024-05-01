import MySQLdb,os
import random
from app import app
from flask import render_template,request

db= MySQLdb.connect(host='localhost',user='root',password='1234', db='izen')
cur = db.cursor()
sql = "insert into score_tbl(math,eng,korea,total,avg,grade) values (%s,%s,%s,%s,%s,%s)"


@app.route('/')
def hello_world():
    return render_template('3.html')


# def getTotalAndAvg(i):
#     return (sum(i), sum(i)/len(i))
# def calcGrade(i):
#     if i>90: return '수'
#     elif i>=80: return '우'
#     elif i>=70: return '미'
#     elif i>=60: return '양'
#     else: return '가'

# for i in range(100):
#     t = tuple()
#     for j in range(3):
#         t += (random.randint(1, 100),)
#         total, avg = getTotalAndAvg(t)
#     t += (total, avg, calcGrade(avg),)
#     print(t)
#     cur.execute(sql, t)
# db.commit()

if __name__=='__main__':
    app.run("0.0.0.0",port=os.getenv('PORT',6969))