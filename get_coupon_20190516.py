import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import pandas as pd

url = "https://www.4freeapp.com/"
respond = requests.get(url,headers={'User-agent': 'Mozilla/5.0'})
html = BeautifulSoup(respond.text)
main = html.find_all("div",class_ = "caption")

#準備空的 dataFrame
df = pd.DataFrame(columns=['id','title','class','content'])
df1 = pd.DataFrame(columns=['title','adress'])


#儲存網頁內所有內容
add_String=''
add_Tag = ''

todayjudge = ''


for _ in main:
    indextitle = _.find("a").string  # 這個會有\n
    indexurl = _.find("a").get("href")
    IndexTitle = indextitle.split('\n')[1]
    #judge the url
    todayjudge  = indexurl

    indexrespond = requests.get(indexurl, headers={'User-agent': 'Mozilla/5.0'})
    # print(indexrespond)
    indexhtml = BeautifulSoup(indexrespond.text)
    indexmain = indexhtml.find_all("a", attrs={'style': 'margin-left: 1em; margin-right: 1em;'})
    # print(IndexTitle)  <-直接使用網站的title會有\n的問題，所以要先排除\n或\造成的錯誤("\"會造成註解)
    # print(indexmain[0].get("href"))  #<--這裡是get,因為已經在<a>裡了

    # 網頁內容
    index_content = indexhtml.find_all("span", attrs={'style': 'font-size: large;'})
    #網頁 tag
    indextag = indexhtml.find_all("div", class_="widget-tags")

    #class
    for text in indextag:
        print(IndexTitle)
        text_a = text.find_all("a")

        for str in text_a:
            # 物件類別
            class_tab = str.string
            web_tag = class_tab.split("\n")[1]
            add_Tag = add_Tag + web_tag + "/"


    #content
    for text in index_content:
        if text.string is not None:
            # add_text.append(text.string.splitlines())
            #splitlines將\n分開
            add_String = add_String + text.string.splitlines()[0]+"\ "
    # ID
    for i in indexmain:
        downloadURL = i.get("href")
        ds = downloadURL.split("/")
        ##設定ID
        coupon_id = ds[5]
        s = pd.Series([coupon_id,IndexTitle.splitlines()[-1],add_Tag, add_String], index=['id','title','class','content'])
        df = df.append(s, ignore_index=True)

    # 重製儲存字串
    add_String = ''
    add_Tag = ''

    #儲存圖片
    for i in indexmain:
        #print(IndexTitle)
        # 設定資料夾路徑，怕標題有/
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

print("判斷標準",todayjudge)

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

    # 網頁內容
    index_content = indexhtml.find_all("span", attrs={'style': 'font-size: large;'})
    # 網頁 tag
    indextag = indexhtml.find_all("div", class_="widget-tags")


    for times in reversed(main):
        indextitle = times.find("a").string #這個會有\n
        indexurl = times.find("a").get("href")
        IndexTitle = indextitle.split('\n')[1]  ##把indextitle的\n排除
        # print(indextitle)
        # print(indexurl)

        if todayjudge == indexurl:
            todayjudge  = main[-1].find("a").get("href")
            break


        print("頁尾",main[-1].find("a").get("href"))
        print("判斷標準",todayjudge)
        print(IndexTitle)

        indexrespond = requests.get(indexurl,headers={'User-agent': 'Mozilla/5.0'})
        # print(indexrespond)
        indexhtml = BeautifulSoup(indexrespond.text)
        indexmain = indexhtml.find_all("a",attrs = {'style':'margin-left: 1em; margin-right: 1em;'})
        # print(IndexTitle)  <-直接使用網站的title會有\n的問題，所以要先排除\n或\造成的錯誤("\"會造成註解)
        # print(indexmain[0].get("href"))  <--這裡是get,因為已經在<a>裡了

        # 網頁內容
        index_content = indexhtml.find_all("span", attrs={'style': 'font-size: large;'})

        # 將標題和內容存成CSV
        for text in index_content:
            if text.string is not None:
                # add_text.append(text.string.splitlines())
                # splitlines將\n分開
                add_String = add_String + text.string.splitlines()[0] + "\ "

        # class
        for text in indextag:
            print(IndexTitle)
            text_a = text.find_all("a")

            for str in text_a:
                # 物件類別
                class_tab = str.string
                web_tag = class_tab.split("\n")[1]
                add_Tag = add_Tag + web_tag + "/"
        # ID
        for i in indexmain:
            downloadURL = i.get("href")
            ds = downloadURL.split("/")
            ##設定ID
            coupon_id = ds[5]
            print(coupon_id)
            s = pd.Series([coupon_id, IndexTitle.splitlines()[-1], add_Tag, add_String],
                          index=['id', 'title', 'class', 'content'])
            df = df.append(s, ignore_index=True)

        # 重製儲存字串
        add_String = ''
        add_Tag = ''

        ##儲存
        for i in indexmain:
            print(IndexTitle)
            # 設定資料夾路徑，怕標題有/
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