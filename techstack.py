import requests,json
from bs4 import BeautifulSoup

userUrl = 'upes.ac.in'
# url = "https://sitereport.netcraft.com/?url=https://google.com&ajax=dcg"
url = f"https://sitereport.netcraft.com/?url=http://{userUrl}&ajax=dcg"
 
response = requests.get(url)
jsonResp = json.loads(response.content)["technology_table"]
# print(jsonResp)

soup = BeautifulSoup(jsonResp, "lxml")
techStackList = soup.find(class_="technology_list").find_all('li')
for i in techStackList:
    if (i.find(class_="section_subtitle").text.strip() == "Server-Side"):
        print("Server-Side")
        for tdData in i.find('tbody').find_all('tr'):
            print(tdData.find('td').text)

    elif (i.find(class_="section_subtitle").text.strip() == "Client-Side"):
        print("Client-Side")
        for tdData in i.find('tbody').find_all('tr'):
            print(tdData.find('td').text)