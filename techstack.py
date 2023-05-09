import requests,json
from bs4 import BeautifulSoup

def techStackFunc(userUrl):
    print("I am here")
    # requests.post("http://127.0.0.1:5000/help",json={"testurl":"test text"})
    print("I am here too")
    url = f"https://sitereport.netcraft.com/?url=http://{userUrl}&ajax=dcg"
    
    response = requests.get(url)
    jsonResp = json.loads(response.content)["technology_table"]
    # print(jsonResp)
    techStackDict  = {"Server-Side":[],"Client-Side":[]}
    serverSideList = []
    clientSideList = []

    soup = BeautifulSoup(jsonResp, "lxml")
    techStackList = soup.find(class_="technology_list").find_all('li')
    
    for i in techStackList:
        if (i.find(class_="section_subtitle").text.strip() == "Server-Side"):
            print("Server-Side")
            for tdData in i.find('tbody').find_all('tr'):
                # print(tdData.find('td').text)
                techStackDict["Server-Side"].append(tdData.find('td').text)
                # serverSideList.append(tdData.find('td').text)
                # requests.post("http://127.0.0.1:5000/techstack",json={'serverSideData':tdData.find('td').text})

        elif (i.find(class_="section_subtitle").text.strip() == "Client-Side"):
            print("Client-Side")
            for tdData in i.find('tbody').find_all('tr'):
                # print(tdData.find('td').text)
                techStackDict["Client-Side"].append(tdData.find('td').text)
                # clientSideList.append(tdData.find('td').text)
                # requests.post("http://127.0.0.1:5000/techstack",json={'clientSideData':tdData.find('td').text})
    print(json.dumps(techStackDict))
    requests.post("http://127.0.0.1:5000/techstackdata",json=json.dumps(techStackDict))