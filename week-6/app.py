import mysql.connector
from mysql.connector import Error 


from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
) #建立Application物件@app.route("/signin",methods=["POST"])
db=mysql.connector.connect(
    host="localhost", #主機名稱
    user="root", #帳號
    password="12345678", #密碼
    database="website" #資料庫名稱
)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["POST"])
def signup():
    #從前端接收資料
    nickname=request.form["nickname"]
    username=request.form["username"]
    password=request.form["password"]
    #根據接收到的資料跟資料庫互動
    cursor=db.cursor()
    #檢查會員集合中是否有相同資料
    cursor.execute("select username from member where username=%s",[username])
    records=cursor.fetchone()

    result1="帳號已經被註冊"
    if  records != None :
        return redirect(url_for("error",message=result1))

    sql="insert into member(name,username,password) values (%s,%s,%s)"
    newdata=(nickname,username,password)
    cursor=db.cursor()
    cursor.execute(sql, newdata)
    db.commit()
    return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html", data=request.args.get("message"))

@app.route("/signin",methods=["POST"])
def signin():
    #從前端接收資料
    username=request.form["username"]
    password=request.form["password"]
    #根據接收到的資料跟資料庫互動
    cursor=db.cursor()
    #檢查會員集合中是否有相同資料
    cursor.execute("select name,username,password from member where username=%s and password =%s ",[username,password])
    rec=cursor.fetchone()
  

    result="帳號或密碼錯誤"
    if rec == None  :
        return redirect(url_for("error",message=result))
    else:
        session["username"]=request.form["username"]
        session["nickname"]=rec[0]
        return redirect("/member") 

app.secret_key="any string but secret"

@app.route("/member")
def member(): 
    if "username" in session:
        return render_template("member.html",data=session["nickname"])
    else:
        return redirect("/")   

@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")

app.run(port=3000) #透過port改變埠號

