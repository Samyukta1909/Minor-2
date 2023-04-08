import subprocess,re


def hiddenFiles(targetName):
    result = subprocess.check_output(['waybackurls',targetName,'|','uniq'])
    hidFilesList = []
    for i in (re.findall(r'(.*\.js|.*\.php|.*\.txt)',str(result.decode('utf-8')))):
        # print(i)
        hidFilesList.append(i)
    # print(result)

    return hidFilesList