import subprocess,re,requests

def hiddenFiles(targetName):
    print("Hiddenfile started")
    result = subprocess.check_output(['waybackurls',targetName,'|','uniq'])
    hidFilesList = []
    for i in (re.findall(r'(.*\.js|.*\.php|.*\.txt)',str(result.decode('utf-8')))):
        hidFilesList.append(i)

    requests.post('http://127.0.0.1:5000/senstiveUrls', json={'urls':hidFilesList})
    
