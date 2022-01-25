使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

insert into member(name,username,password)-> values('winnie','test','test','500');
insert into member(name,username,password)-> values('jack','qazwsx','123456''300');
insert into member(name,username,password)-> values('john','qweasd','q123456','200');
insert into member(name,username,password) -> values('jenny','a11111','a789456','600');
insert into member(name,username,password)-> values('mary','winei','e111e42e','200');

使用 SELECT 指令取得所有在 member 資料表中的會員資料。
select * from member;
![image](https://user-images.githubusercontent.com/92582911/150930237-dfd7f567-0228-4b38-8aae-e19aa95d4ba1.png)

使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
 select * from member order by time desc;
![image](https://user-images.githubusercontent.com/92582911/150930354-225177b7-63b4-46bd-a758-5ae34b40cf67.png)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
select * from member order by time desc LIMIT 1, 3;
![image](https://user-images.githubusercontent.com/92582911/150932544-81678137-db7b-4128-aa3f-4a300cf358df.png)

使用 SELECT 指令取得欄位 username 是 test 的會員資料。
select * from member where username='test';
![image](https://user-images.githubusercontent.com/92582911/150932764-6403e8a0-c206-427b-9529-5dd001c4d80d.png)

使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
select * from member where username='test' and password='test';
![image](https://user-images.githubusercontent.com/92582911/150932931-09375db0-1607-4c9e-9401-5a9a9e2e89d8.png)

使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
update member set name='test2' where username='test';
![image](https://user-images.githubusercontent.com/92582911/150933811-78891f52-77ff-4e72-af41-d14b42988951.png)

取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
select count(name) from member;
![image](https://user-images.githubusercontent.com/92582911/150934266-9e83e6af-7d28-4145-9d4c-7b8c1b47b669.png)

取得 member 資料表中，所有會員 follower_count 欄位的總和。
select sum(follower_count) from member;
![image](https://user-images.githubusercontent.com/92582911/150934503-667eca13-3a07-4b65-a2e0-0d46249b3d71.png)

取得 member 資料表中，所有會員 follower_count 欄位的平均數。
select sum(follower_count)/count(name) from member;
![image](https://user-images.githubusercontent.com/92582911/150934757-e0f492fb-917b-44c9-8f0b-906a8d50f51d.png)

