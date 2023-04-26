from requests_html import HTMLSession
import json,requests


def headlines():
    print("News file started")
    session = HTMLSession()

    url= "https://www.bleepingcomputer.com/#nlatest"
    r= session.get(url)
    # r.html.render(sleep=1, scrolldown=5)

    articles = r.html.find('li')
    #print(articles)

    newslist =[]

    for item in articles:
        try:
            news=item.find('h4', first=True)
            title= news.text
            link= list(news.absolute_links)[0]
            newslist.append([title,link])
        except:
            pass

    requests.post('http://127.0.0.1:5000/news', json={'news':newslist})
    # return (newslist)

# headlines()