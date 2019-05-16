import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import pandas as pd

url = "https://www.4freeapp.com/"
respond = requests.get(url,headers={'User-agent': 'Mozilla/5.0'})
html = BeautifulSoup(respond.text)
main = html.find_all("div",class_ = "caption")

#�ǳƪŪ� dataFrame
df = pd.DataFrame(columns=['id','title','class','content'])
df1 = pd.DataFrame(columns=['title','adress'])


#�x�s�������Ҧ����e
add_String=''
add_Tag = ''

todayjudge = ''


for _ in main:
    indextitle = _.find("a").string  # �o�ӷ|��\n
    indexurl = _.find("a").get("href")
    IndexTitle = indextitle.split('\n')[1]
    #judge the url
    todayjudge  = indexurl

    indexrespond = requests.get(indexurl, headers={'User-agent': 'Mozilla/5.0'})
    # print(indexrespond)
    indexhtml = BeautifulSoup(indexrespond.text)
    indexmain = indexhtml.find_all("a", attrs={'style': 'margin-left: 1em; margin-right: 1em;'})
    # print(IndexTitle)  <-�����ϥκ�����title�|��\n�����D�A�ҥH�n���ư�\n��\�y�������~("\"�|�y������)
    # print(indexmain[0].get("href"))  #<--�o�̬Oget,�]���w�g�b<a>�̤F

    # �������e
    index_content = indexhtml.find_all("span", attrs={'style': 'font-size: large;'})
    #���� tag
    indextag = indexhtml.find_all("div", class_="widget-tags")

    #class
    for text in indextag:
        print(IndexTitle)
        text_a = text.find_all("a")

        for str in text_a:
            # �������O
            class_tab = str.string
            web_tag = class_tab.split("\n")[1]
            add_Tag = add_Tag + web_tag + "/"


    #content
    for text in index_content:
        if text.string is not None:
            # add_text.append(text.string.splitlines())
            #splitlines�N\n���}
            add_String = add_String + text.string.splitlines()[0]+"\ "
    # ID
    for i in indexmain:
        downloadURL = i.get("href")
        ds = downloadURL.split("/")
        ##�]�wID
        coupon_id = ds[5]
        s = pd.Series([coupon_id,IndexTitle.splitlines()[-1],add_Tag, add_String], index=['id','title','class','content'])
        df = df.append(s, ignore_index=True)

    # ���s�x�s�r��
    add_String = ''
    add_Tag = ''

    #�x�s�Ϥ�
    for i in indexmain:
        #print(IndexTitle)
        # �]�w��Ƨ����|�A�ȼ��D��/
        dname = "C:/Users/case-pc/Desktop/coupon/" + IndexTitle.split("/")[0] + "/"

        if not os.path.exists(dname):
            os.mkdir(dname)

        downloadURL = i.get("href")
        print(downloadURL)
        ds = downloadURL.split("/")
        filetype = ds[-1].split(".")[-1]
        judgeURL = filetype
        # print(ds[5])
        if judgeURL:
            fpath = dname + ds[5] + "." + filetype
            urlretrieve(downloadURL, fpath)
        s1 = pd.Series([IndexTitle.splitlines()[-1],fpath],index=['title','adress'])
        df1 = df1.append(s1,ignore_index=True)

print("�P�_�з�",todayjudge)

def judge(x):
    if "jpg" in x or "png" in x:
        return True
    else:
        return False

import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d")
now = now.split("-")
begin = datetime.date(int(now[0]),int(now[1]),int(now[2]))
end = datetime.date(2019,5,11)
d = begin
delta = datetime.timedelta(days=1)

while d >= end:
    print(d.strftime("%Y-%m-%d"))
    url = "https://www.4freeapp.com/search?updated-max="+d.strftime("%Y-%m-%d")+"T10%3A53%3A00%2B08%3A00&max-results=7#PageNo=2"
    respond = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    # print(respond)

    html = BeautifulSoup(respond.text)
    main = html.find_all("div", class_="caption")
    # print(main[0].find("a").get("href"))

    # �������e
    index_content = indexhtml.find_all("span", attrs={'style': 'font-size: large;'})
    # ���� tag
    indextag = indexhtml.find_all("div", class_="widget-tags")


    for times in reversed(main):
        indextitle = times.find("a").string #�o�ӷ|��\n
        indexurl = times.find("a").get("href")
        IndexTitle = indextitle.split('\n')[1]  ##��indextitle��\n�ư�
        # print(indextitle)
        # print(indexurl)

        if todayjudge == indexurl:
            todayjudge  = main[-1].find("a").get("href")
            break


        print("����",main[-1].find("a").get("href"))
        print("�P�_�з�",todayjudge)
        print(IndexTitle)

        indexrespond = requests.get(indexurl,headers={'User-agent': 'Mozilla/5.0'})
        # print(indexrespond)
        indexhtml = BeautifulSoup(indexrespond.text)
        indexmain = indexhtml.find_all("a",attrs = {'style':'margin-left: 1em; margin-right: 1em;'})
        # print(IndexTitle)  <-�����ϥκ�����title�|��\n�����D�A�ҥH�n���ư�\n��\�y�������~("\"�|�y������)
        # print(indexmain[0].get("href"))  <--�o�̬Oget,�]���w�g�b<a>�̤F

        # �������e
        index_content = indexhtml.find_all("span", attrs={'style': 'font-size: large;'})

        # �N���D�M���e�s��CSV
        for text in index_content:
            if text.string is not None:
                # add_text.append(text.string.splitlines())
                # splitlines�N\n���}
                add_String = add_String + text.string.splitlines()[0] + "\ "

        # class
        for text in indextag:
            print(IndexTitle)
            text_a = text.find_all("a")

            for str in text_a:
                # �������O
                class_tab = str.string
                web_tag = class_tab.split("\n")[1]
                add_Tag = add_Tag + web_tag + "/"
        # ID
        for i in indexmain:
            downloadURL = i.get("href")
            ds = downloadURL.split("/")
            ##�]�wID
            coupon_id = ds[5]
            print(coupon_id)
            s = pd.Series([coupon_id, IndexTitle.splitlines()[-1], add_Tag, add_String],
                          index=['id', 'title', 'class', 'content'])
            df = df.append(s, ignore_index=True)

        # ���s�x�s�r��
        add_String = ''
        add_Tag = ''

        ##�x�s
        for i in indexmain:
            print(IndexTitle)
            # �]�w��Ƨ����|�A�ȼ��D��/
            dname = "C:/Users/case-pc/Desktop/coupon/" + IndexTitle.split("/")[0] + "/"
            if not os.path.exists(dname):
                os.mkdir(dname)

            downloadURL = i.get("href")
            print(downloadURL)

            ds = downloadURL.split("/")
            filetype = ds[-1].split(".")[-1]
            # print(ds[5])
            if judge(filetype):
                fpath = dname + ds[5] + "." + filetype
                urlretrieve(downloadURL, fpath)
            s1 = pd.Series([IndexTitle.splitlines()[-1], fpath], index=['title', 'adress'])
            df1 = df1.append(s1, ignore_index=True)

    d -= delta
print(df)
print(df1)
df.to_csv("title_content.csv",encoding='utf-8',index=False)
df1.to_csv("title_address.csv",encoding='utf-8',index=False)