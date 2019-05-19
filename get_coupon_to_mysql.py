import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import pandas as pd

#��Ʈw�s��
import mysql.connector
from insert_mysql import prevent_duplicate

#--------�o��u�O�n��J�K�X----------------
from password import My_password


#�إ߸�Ʈw�s�u
mydb = mysql.connector.connect(
    user='root',
    passwd=My_password,
    host='localhost',
    database='mangerdb',
)

mycursor = mydb.cursor()
mycursor.execute('use mangerdb')

url = "https://www.4freeapp.com/"
respond = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
html = BeautifulSoup(respond.text)
main = html.find_all("div", class_="caption")

# �ǳƪŪ� dataFrame
df = pd.DataFrame(columns=['id', 'title', 'class', 'content'])
df1 = pd.DataFrame(columns=['title', 'adress'])

# �x�s�������Ҧ����e
add_String = ''
add_Tag = ''

today_judge = ''


# �P�_�ɦW
def judge(x):
    if "jpg" in x or "png" in x:
        return True
    else:
        return False


for _ in main:
    index_title = _.find("a").string  # �o�ӷ|��\n
    index_url = _.find("a").get("href")

    # �����ϥκ�����title�|��\n�����D�A�ҥH�n���ư�\n��\�y�������~("\"�|�y������)
    Index_Title = index_title.split('\n')[1]
    # judge the url
    today_judge = index_url

    index_respond = requests.get(index_url, headers={'User-agent': 'Mozilla/5.0'})
    index_html = BeautifulSoup(index_respond.text)
    index_main = index_html.find_all("a", attrs={'style': 'margin-left: 1em; margin-right: 1em;'})

    # �������e
    index_content = index_html.find_all("span", attrs={'style': 'font-size: large;'})

    # ���� tag
    index_tag = index_html.find_all("div", class_="widget-tags")

    # MySQL Myclass
    for text in index_tag:
        print(Index_Title)
        text_a = text.find_all("a")

        for str in text_a:
            # �������O
            class_tab = str.string
            web_tag = class_tab.split("\n")[1]
            add_Tag = add_Tag + web_tag + "/"

    # MySQL content
    for text in index_content:
        if text.string is not None:
            # add_text.append(text.string.splitlines())
            # splitlines�N\n���}
            add_String = add_String + text.string.splitlines()[0] + "\ "

    # MySQL ID
    for i in index_main:
        downloadURL = i.get("href")
        ds = downloadURL.split("/")
        ##�]�wID
        coupon_id = ds[5]

        #�N��ƿ�J�i��Ʈw
        prevent_duplicate(coupon_id, Index_Title.splitlines()[-1], add_Tag, add_String)

        #�N��Ʀs�JDataFrame
        s = pd.Series([coupon_id, Index_Title.splitlines()[-1], add_Tag, add_String],
                      index=['id', 'title', 'class', 'content'])
        df = df.append(s, ignore_index=True)

    # ���s�x�s�r��
    add_String = ''
    add_Tag = ''

    # �x�s�Ϥ�
    for i in index_main:
        # �]�w��Ƨ����|�A�ȼ��D��/
        dname = "C:/Users/Jun/Desktop/coupon/" + Index_Title.split("/")[0] + "/"

        if not os.path.exists(dname):
            os.mkdir(dname)

        downloadURL = i.get("href")
        print(downloadURL)
        ds = downloadURL.split("/")
        filetype = ds[-1].split(".")[-1]
        judgeURL = filetype

        if judgeURL:
            fpath = dname + ds[5] + "." + filetype
            urlretrieve(downloadURL, fpath)

        s1 = pd.Series([Index_Title.splitlines()[-1], fpath], index=['title', 'adress'])
        df1 = df1.append(s1, ignore_index=True)

print("�P�_�з�", today_judge)

import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d")
now = now.split("-")
begin = datetime.date(int(now[0]), int(now[1]), int(now[2]))
end = datetime.date(2019, 5, 11)
d = begin
delta = datetime.timedelta(days=1)

while d >= end:
    print(d.strftime("%Y-%m-%d"))
    url = "https://www.4freeapp.com/search?updated-max=" + d.strftime(
        "%Y-%m-%d") + "T10%3A53%3A00%2B08%3A00&max-results=7#PageNo=2"
    respond = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

    html = BeautifulSoup(respond.text)
    main = html.find_all("div", class_="caption")

    # �������e
    index_content = index_html.find_all("span", attrs={'style': 'font-size: large;'})
    # ���� tag
    index_tag = index_html.find_all("div", class_="widget-tags")

    for times in reversed(main):
        index_title = times.find("a").string  # �o�ӷ|��\n
        index_url = times.find("a").get("href")
        Index_Title = index_title.split('\n')[1]  ##��indextitle��\n�ư�

        if today_judge == index_url:
            today_judge = main[-1].find("a").get("href")
            break

        print("����", main[-1].find("a").get("href"))
        print("�P�_�з�", today_judge)
        print(Index_Title)

        index_respond = requests.get(index_url, headers={'User-agent': 'Mozilla/5.0'})
        index_html = BeautifulSoup(index_respond.text)
        index_main = index_html.find_all("a", attrs={'style': 'margin-left: 1em; margin-right: 1em;'})

        # �������e
        index_content = index_html.find_all("span", attrs={'style': 'font-size: large;'})

        # �N���D�M���e�s��CSV
        for text in index_content:
            if text.string is not None:
                # add_text.append(text.string.splitlines())
                # splitlines�N\n���}
                add_String = add_String + text.string.splitlines()[0] + "\ "

        # MySQL Myclass
        for text in index_tag:
            print(Index_Title)
            text_a = text.find_all("a")

            for str in text_a:
                # �������O
                class_tab = str.string
                web_tag = class_tab.split("\n")[1]
                add_Tag = add_Tag + web_tag + "/"
        # MySQL ID
        for i in index_main:
            downloadURL = i.get("href")
            ds = downloadURL.split("/")
            ##�]�wID
            coupon_id = ds[5]
            print(coupon_id)

            # �N��ƿ�J�i��Ʈw
            prevent_duplicate(coupon_id, Index_Title.splitlines()[-1], add_Tag, add_String)

            #�N��Ʀs�iDataFrame
            s = pd.Series([coupon_id, Index_Title.splitlines()[-1], add_Tag, add_String],
                          index=['id', 'title', 'class', 'content'])
            df = df.append(s, ignore_index=True)

        # ���s�x�s�r��
        add_String = ''
        add_Tag = ''

        ##�x�s
        for i in index_main:
            print(Index_Title)
            # �]�w��Ƨ����|�A�ȼ��D��/
            dname = "C:/Users/Jun/Desktop/coupon/" + Index_Title.split("/")[0] + "/"
            if not os.path.exists(dname):
                os.mkdir(dname)

            downloadURL = i.get("href")
            print(downloadURL)

            ds = downloadURL.split("/")
            filetype = ds[-1].split(".")[-1]
            if judge(filetype):
                fpath = dname + ds[5] + "." + filetype
                urlretrieve(downloadURL, fpath)

            s1 = pd.Series([Index_Title.splitlines()[-1], fpath], index=['title', 'adress'])
            df1 = df1.append(s1, ignore_index=True)

    d -= delta
print(df)
print(df1)
df.to_csv("title_content.csv", encoding='utf-8', index=False)
df1.to_csv("title_address.csv", encoding='utf-8', index=False)