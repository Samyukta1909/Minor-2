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
            except:
                pass  

    return endpointsList