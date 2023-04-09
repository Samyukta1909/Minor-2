import requests
import concurrent.futures


def endpoint(targetname):
    endpointsList=[]
    with open('static/endpointstestfile.txt') as f:
        for i in f.readlines():
            s="https://"+targetname+"/"+i.strip()
            try:
                r = requests.get(url=s)
                if(r.status_code==200 or r.status_code==301 or r.status_code==302):
                    endpointsList.append(s)
                    requests.post('http://127.0.0.1:5000/endpointUrls', json={'urls':s})
            except:
                pass  

  