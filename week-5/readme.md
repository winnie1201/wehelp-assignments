使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

insert into member(name,username,password)-> values('winnie','test','test','500');
insert into member(name,username,password)-> values('jack','qazwsx','123456''300');
insert into member(name,username,password)-> values('john','qweasd','q123456','200');
insert into member(name,username,password) -> values('jenny','a11111','a789456','600');
insert into member(name,username,password)-> values('mary','winei','e111e42e','200');

使用 SELECT 指令取得所有在 member 資料表中的會員資料。
select * from member;

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/1.JPG)

使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
 select * from member order by time desc;
 
![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/2.JPG)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
select * from member order by time desc LIMIT 1, 3;

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/3.JPG)

使用 SELECT 指令取得欄位 username 是 test 的會員資料。
select * from member where username='test';

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/4.JPG)

使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
select * from member where username='test' and password='test';

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/5.JPG)

使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
update member set name='test2' where username='test';

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/6.JPG)

取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
select count(name) from member;

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/7.JPG)

取得 member 資料表中，所有會員 follower_count 欄位的總和。
select sum(follower_count) from member;

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/8.JPG)

取得 member 資料表中，所有會員 follower_count 欄位的平均數。
select sum(follower_count)/count(name) from member;

![image](https://github.com/winnie1201/wehelp-assignments/blob/main/week-5/9.JPG)

