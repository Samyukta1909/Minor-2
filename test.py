import requests

params = {'test':'test text'}

def testfunc():
    print("calling test func")
    requests.post("http://127.0.0.1:5000/senstiveUrls",json=params)
    print("test func called")
