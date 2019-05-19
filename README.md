# MySQL connector&python install

###### tags: `SQL` `python` 

**官方網站:** https://dev.mysql.com/downloads/connector/python/

**安裝參考網站:**
https://www.w3schools.com/python/python_mysql_getstarted.asp

我們要選64bit,32bit會安裝不起來!!!

![](https://i.imgur.com/Ebam1rR.png)

**自學網站:** https://www.w3schools.com/python/python_mysql_create_db.asp

測試連接
```
import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='passwd'
)
print(mydb)
```
結果(表示連接成功)
```
<mysql.connector.connection.MySQLConnection object ar 0x016645F0>
```

## 出現Authentication plugin 'caching_sha2_password' is not supported錯誤時


參考:https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported

使用以下指令
```
pip install mysql-connector-python
```

# 實際編寫SQL指令

## 基本操作
### cursor(可以把他想成鼠標)，可以透過execute來執行Raw SQL

下面是選取資料的範例
![](https://i.imgur.com/2e38XiL.png)


### Insert

範例:
![](https://i.imgur.com/A58Y9Mi.png)

實際測試:
先使用mangerdb，因為我們資料存在這個地方
最後用print，來看看有幾個資料被輸入進去了
![](https://i.imgur.com/aAd6mNY.png)

### fetchone & fetchall
![](https://i.imgur.com/J0CMSI2.png)

### 使用 %s 注意事項(是用tuple傳遞)

所以我們要將要輸入進去的%s，以tuple的方式傳遞進去，而完成後是不會有任何東西，還要透過fetchall來返回多個tuple!!!
這時候是以JSON回傳，因為我們是使用fetchall來返回多個
(如果使用fetchone就只會返回一個)

![](https://i.imgur.com/vMwTheH.png)

### 實際判斷是否重複

透過回傳id值,如果被搜尋的到，代表資料庫已經擁有
反之，回傳沒有，代表資料庫沒有，故我們可以寫入
![](https://i.imgur.com/aVmBujb.png)

