import requests
import concurrent.futures


def subdomain(targetname):
    subdomainList=[]
    with open('static/textfile.txt') as f:
        for i in f.readlines():
            s="https://"+i.strip()+"."+targetname
            try:
                r = requests.get(url=s)
                if(r.status_code==200 or r.status_code==301 or r.status_code==302):
                    subdomainList.append(s)
            except:
                pass  

    return subdomainList