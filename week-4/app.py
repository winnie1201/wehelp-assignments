#初始化資料庫連線
import pymongo
client=pymongo.MongoClient("mongodb://root:root123@mycluster.whiup.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test #選擇操作test資料庫
print("資料庫連線建立成功")

from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
) #建立Application物件@app.route("/signin",methods=["POST"])

@app.route("/signin",methods=["POST"])
def signin():
    #從前端取得使用者的輸入
    username=request.form["username"]
    password=request.form["password"]
    
    result="請輸入帳號、密碼"
    result1="帳號或密碼輸入錯誤"
    #輸入錯誤，登入失敗，導向到錯誤頁面
    if (username == "" or username == None) and (password == "" or password == None):
        return redirect(url_for("error",message=result))   
    if username != "test" and password != "test":
        return redirect(url_for("error",message=result1)) 
    if username == "test" and password != "test":
        return redirect(url_for("error",message=result1)) 
    if username != "test" and password == "test":
        return redirect(url_for("error",message=result1)) 
    if username == "test" and password == "test":
        session["username"]=request.form["username"]
        return redirect("/member")  
    
    
    
   


app.secret_key="any string but secret"
#處理路由
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("/")

#/error?msg=錯誤訊息
@app.route("/error")
def error():
    return render_template("error.html", data=request.args.get("message"))


@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")

app.run(port=3000) #透過port改變埠號