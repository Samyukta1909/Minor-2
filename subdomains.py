import requests
import threading

# subdomain_thread_stop_event = threading.Event()
subdomainList=[]
def subdomain(targetname):
    # subdomainList=[]
    str="Target Name: "+targetname
    subdomainList.append(str)
    subdomain_count=0
    with open('static/textfile.txt') as f:
        for i in f.readlines():
            s="https://"+i.strip()+"."+targetname
            try:
                r = requests.get(url=s)
                if(r.status_code==200 or r.status_code==301 or r.status_code==302):
                    subdomainList.append(s)
                   
                    requests.post('http://127.0.0.1:5000/subdomainUrls', json={'urls':s})
                    
            except:
                pass  

    #return subdomainList