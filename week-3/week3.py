import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]
s="景點名稱,區域,經度,緯度,第一張圖檔網址\n"
for clists in clist:
        print(clists["stitle"],clists["address"][5:8],clists["longitude"],clists["latitude"])
        print(clists["file"].lower().replace('jpg','jpg\n').split("\n")[0])
        s+="{},{},{},{},{}\n".format(clists["stitle"],clists["address"][5:8],clists["longitude"],clists["latitude"],clists["file"].lower().replace('jpg','jpg\n').split("\n")[0])
fw=open("week3.csv","w",encoding="utf-8")
fw.write(s)
fw.close()

