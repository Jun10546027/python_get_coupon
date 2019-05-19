# MySQL connector&python install

###### tags: `SQL` `python` 

**�x�����:** https://dev.mysql.com/downloads/connector/python/

**�w�˰ѦҺ���:**
https://www.w3schools.com/python/python_mysql_getstarted.asp

�ڭ̭n��64bit,32bit�|�w�ˤ��_��!!!

![](https://i.imgur.com/Ebam1rR.png)

**�۾Ǻ���:** https://www.w3schools.com/python/python_mysql_create_db.asp

���ճs��
```
import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='passwd'
)
print(mydb)
```
���G(��ܳs�����\)
```
<mysql.connector.connection.MySQLConnection object ar 0x016645F0>
```

## �X�{Authentication plugin 'caching_sha2_password' is not supported���~��


�Ѧ�:https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported

�ϥΥH�U���O
```
pip install mysql-connector-python
```

# ��ڽs�gSQL���O

## �򥻾ާ@
### cursor(�i�H��L�Q������)�A�i�H�z�Lexecute�Ӱ���Raw SQL

�U���O�����ƪ��d��
![](https://i.imgur.com/2e38XiL.png)


### Insert

�d��:
![](https://i.imgur.com/A58Y9Mi.png)

��ڴ���:
���ϥ�mangerdb�A�]���ڭ̸�Ʀs�b�o�Ӧa��
�̫��print�A�Ӭݬݦ��X�Ӹ�ƳQ��J�i�h�F
![](https://i.imgur.com/aAd6mNY.png)

### fetchone & fetchall
![](https://i.imgur.com/J0CMSI2.png)

### �ϥ� %s �`�N�ƶ�(�O��tuple�ǻ�)

�ҥH�ڭ̭n�N�n��J�i�h��%s�A�Htuple���覡�ǻ��i�h�A�ӧ�����O���|������F��A�٭n�z�Lfetchall�Ӫ�^�h��tuple!!!
�o�ɭԬO�HJSON�^�ǡA�]���ڭ̬O�ϥ�fetchall�Ӫ�^�h��
(�p�G�ϥ�fetchone�N�u�|��^�@��)

![](https://i.imgur.com/vMwTheH.png)

### ��ڧP�_�O�_����

�z�L�^��id��,�p�G�Q�j�M����A�N���Ʈw�w�g�֦�
�Ϥ��A�^�ǨS���A�N���Ʈw�S���A�G�ڭ̥i�H�g�J
![](https://i.imgur.com/aVmBujb.png)

