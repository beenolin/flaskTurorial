from flask import Flask,render_template
import MySQLdb,os

from flask import render_template,request

app = Flask(__name__)
db= MySQLdb.connect(host='localhost',user='root',password='1234', db='free_board')
cur = db.cursor()

sql = "select * from board"
cur.execute(sql)
data_list = cur.fetchall()
print(data_list[0])
print(data_list[1])
print(data_list[2])


@app.route('/')
def index():
    return render_template('index.html',data_list=data_list)
@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/delete")
def delete():
    no = request.args.get('num');
    print(no)
    cur.execute("delete from board where num='" + no + "'")
    db.commit()
    sql="select * from board"
    cur.execute(sql)
    data_list = cur.fetchall()
    return render_template("index.html",data_list=data_list)

@app.route("/get")
def get():
    no = request.args.get('no');
    print(no)
    cur.execute("select * from board where num='" + no + "'")
    result = cur.fetchone();
    print(result)
    return render_template("get.html",result=result)

@app.route("/insert",methods=['POST'])
def insertpost():
    if request.method == 'POST':

        #num,title,writer,views,context
        result = request.form
        dict_gui = result.to_dict()
        print(dict_gui)
        t = tuple()
        for j,v in dict_gui.items():
            t+=(v,)
        sql = "insert into board values (%s,%s,%s,%s,%s)"
        cur.execute(sql,t)
        db.commit()

        sql = "select * from board"
        cur.execute(sql)
        data_list = cur.fetchall()
        for i in data_list:
            print(i)


    return render_template('index.html',data_list=data_list)
if __name__=='__main__':
    app.run()